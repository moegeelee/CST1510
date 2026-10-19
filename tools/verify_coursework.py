"""Verify the worked coursework using Python's standard library.

Run from any folder: python3 /absolute/path/to/tools/verify_coursework.py
Add --save-outputs to store sample execution results in the notebooks.
This verifies code behaviour, not a student's understanding or submission.
The verification tooling uses later Python features; it is not coursework.
"""
import ast
import builtins
import contextlib
from datetime import datetime, timezone
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import random
import shutil
import signal
import subprocess
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SAVE_OUTPUTS = '--save-outputs' in sys.argv
SAVE_WEEK4_OUTPUTS = '--save-week4-outputs' in sys.argv
RESULTS = []
TRANSCRIPTS = []
STATS = {'notebooks': 0, 'code_cells': 0, 'expected_notebook_errors': 0}


def record(name, condition, details=''):
    RESULTS.append({'check': name, 'passed': bool(condition), 'details': details})


def timeout_handler(signum, frame):
    raise TimeoutError('Execution exceeded five seconds; check for an infinite loop.')


@contextlib.contextmanager
def execution_workspace(path):
    """Copy script fixtures so file-writing exercises cannot alter the repository."""
    path = path.resolve()
    week4 = ROOT / 'Week 04 - Lists, Dictionaries and Files'
    base = week4 if path.is_relative_to(week4) else path.parent
    with tempfile.TemporaryDirectory() as tmp:
        destination = Path(tmp) / 'workspace'
        shutil.copytree(base, destination,
                        ignore=shutil.ignore_patterns('.git', '__pycache__', '.ipynb_checkpoints', '*.ipynb', '.DS_Store'))
        yield destination / path.relative_to(base)


@contextlib.contextmanager
def working_directory(path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


@contextlib.contextmanager
def bounded():
    old = signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


def run_code(source, inputs=(), namespace=None, filename='<practice>'):
    ns = namespace if namespace is not None else {'__name__': '__main__'}
    stream = io.StringIO()
    entries = iter(inputs)
    def sample_input(prompt=''):
        try:
            value = next(entries)
        except StopIteration:
            raise AssertionError(f'Unexpected input request: {prompt}') from None
        print(prompt + value)
        return value
    error = None
    with contextlib.redirect_stdout(stream), patch.object(builtins, 'input', sample_input):
        try:
            with bounded():
                exec(compile(source, filename, 'exec'), ns)
        except Exception as exc:
            error = exc
    unused = list(entries)
    return stream.getvalue(), error, ns, unused


def run_notebooks():
    for path in sorted(ROOT.rglob('*.ipynb')):
        if '.ipynb_checkpoints' in path.parts:
            continue
        nb = json.loads(path.read_text())
        if path.name == 'START_HERE.ipynb':
            # This orientation notebook intentionally contains unanswered practice.
            continue
        STATS['notebooks'] += 1
        random.seed(1510)
        namespace = {'__name__': '__main__'}
        execution_count = 0
        save_outputs = SAVE_OUTPUTS or (SAVE_WEEK4_OUTPUTS and 'Week 04 - Lists, Dictionaries and Files' in path.parts)
        with execution_workspace(path) as temporary_path, working_directory(temporary_path.parent):
            for index, cell in enumerate(nb['cells']):
                if cell['cell_type'] != 'code':
                    continue
                STATS['code_cells'] += 1
                execution_count += 1
                source = ''.join(cell.get('source', []))
                meta = cell.get('metadata', {}).get('cst1510', {})
                expected = meta.get('expected_error')
                output, error, namespace, unused = run_code(
                    source, meta.get('sample_inputs', []), namespace,
                    f'{path.name}:cell-{index}')
                actual = type(error).__name__ if error else None
                record(f'{path.name} cell {index}', actual == expected and not unused,
                       f'Expected: {expected or "success"}; actual: {actual or "success"}'
                       + (f'; {error}' if error and actual != expected else '')
                       + (f'; unused inputs: {unused}' if unused else ''))
                if expected:
                    STATS['expected_notebook_errors'] += 1
                if save_outputs:
                    cell['execution_count'] = execution_count
                    cell['outputs'] = []
                    if output:
                        cell['outputs'].append({'output_type': 'stream', 'name': 'stdout',
                                                'text': output.splitlines(keepends=True)})
                    if error:
                        cell['outputs'].append({'output_type': 'error', 'ename': actual,
                                                'evalue': str(error),
                                                'traceback': [f'{actual}: {error}']})
        if save_outputs:
            nb.setdefault('metadata', {})['cst1510_execution'] = {
                'method': 'Sequential Python exec in a fresh namespace per notebook',
                'python_version': sys.version.split()[0],
                'inputs': 'Sample inputs saved in each cell metadata; not student runs',
                'random_seed': 1510,
                'expected_errors': 'Recorded and execution continued for teaching cells'}
            path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n')


def script(path, inputs=(), expected=None, contains=(), absent=()):
    with execution_workspace(path) as temporary_path:
        run = subprocess.run([sys.executable, str(temporary_path)],
                             input='\n'.join(inputs) + ('\n' if inputs else ''),
                             capture_output=True, text=True, timeout=5, cwd=temporary_path.parent)
    success = (run.returncode != 0 and expected in run.stderr) if expected else run.returncode == 0
    success = success and all(s in run.stdout for s in contains)
    success = success and all(s not in run.stdout for s in absent)
    name = f'{path.relative_to(ROOT) if path.is_relative_to(ROOT) else path.name}: inputs={list(inputs)}'
    record(name, success, run.stderr.strip() if not success else (f'Expected {expected}' if expected else ''))
    TRANSCRIPTS.append(f'FILE: {path}\nINPUTS: {list(inputs)!r}\nEXIT: {run.returncode}\n{run.stdout}{run.stderr}')
    return run


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def notebook_cell(name, index, inputs=(), prelude=''):
    path = next(ROOT.rglob(name))
    source = prelude + '\n' + ''.join(json.loads(path.read_text())['cells'][index]['source'])
    out, error, ns, unused = run_code(source, inputs)
    record(f'{name} cell {index} alternate inputs {inputs}', error is None and not unused, str(error or ''))
    return out, ns


def verify_semantics():
    for part, total, label, percent in [('38','250','rows missing','15.2'),('12','400','failed logins','3.0'),('87','120','disk used GB','72.5')]:
        out, ns = notebook_cell('W01_Lab.ipynb',18,[part,total,label])
        record(f'W01 D7 {label} percent and alignment', f'=  {percent} %' in out and f'{label:<15}:' in out)
    for value,expected in [(89.99,False),(90,True),(100,True),(100.01,False)]:
        out,ns=notebook_cell('W02T01_walkthrough.ipynb',16,prelude=f'percent={value}')
        record(f'Inclusive boolean endpoints {value}',out.strip()==str(expected))
    for attempts, expected in [('1','OK'),('2','WARNING'),('3','LOCKED'),('4','LOCKED')]:
        out,ns=notebook_cell('W02T02_walkthrough.ipynb',20,[attempts])
        record(f'Login tier {attempts}',out.splitlines()[-1]==expected)
    out,ns=notebook_cell('W02T03_walkthrough.ipynb',15,['','2','','-1','done'])
    record('Blank sentinel inputs are skipped', ns['total']==1)
    out,ns=notebook_cell('W02_Lab.ipynb',18,['100','100','101','100','99','100'])
    statuses=[line for line in out.splitlines() if line in ('OK','OVER LIMIT')]
    record('W02 D7 strict greater-than boundary',statuses==['OK','OVER LIMIT','OK'])
    out,ns=notebook_cell('W03_Lab.ipynb',40)
    record('count_over exact limit is not over', ns['count_over'](100,101,99)==1)
    record('count_over handles no values', ns['count_over']()==0)
    out,ns=notebook_cell('W03T03_walkthrough.ipynb',17)
    record('split_time returns minutes and seconds, not hours',ns['split_time'](4831)==(80,31))


def verify_projects():
    for week in (1,2,3):
        path=next(ROOT.rglob(f'W0{week}_Lab.ipynb')).parent/'template.py'
        tree=ast.parse(path.read_text())
        forbidden=(ast.If,ast.For,ast.While,ast.FunctionDef) if week==1 else ((ast.FunctionDef,ast.List,ast.ListComp) if week==2 else (ast.List,ast.ListComp))
        record(f'Week {week} stays within required syntax', not any(isinstance(n,forbidden) for n in ast.walk(tree)))
        for label,loaded,total,remaining,percent in [('survey_2026','1187','1200','+13.00','98.92'),('sample','87','100','+13.00','87.00'),('overflow','120','100','-20.00','120.00')]:
            inputs=[label,loaded,total]+([] if week==1 else ['quit'])
            script(path,inputs,contains=(label,remaining,percent))
        script(path,['zero_total','1','0'],expected='ZeroDivisionError')
        script(path,['bad_input','abc'],expected='ValueError')
        if week>1:
            run=script(path,['a','89.99','100','b','90','100','c','100','100','d','101','100','quit'],contains=('OVER LIMIT records: 2',))
            lines=[line.split(':',1)[1].strip() for line in run.stdout.splitlines() if line.startswith('  Status')]
            record(f'Week {week} exact status boundaries and loop',lines==['OK','WARNING','OVER LIMIT','OVER LIMIT'])
            record(f'Week {week} summary once',run.stdout.count('OVER LIMIT records:')==1)
            script(path,['quit'],contains=('OVER LIMIT records: 0',),absent=('Rows loaded:',))
            script(path,[' QuIt '],contains=('OVER LIMIT records: 0',))
        else:
            script(path,['full','100','100'],contains=('Remaining pct :      +0.00 %',))
        if week==3:
            functions=[n for n in tree.body if isinstance(n,ast.FunctionDef)]
            record('Week 3 functions have docstrings',all(ast.get_docstring(n) for n in functions))
            record('Week 3 calculations and status do not print',all(not any(isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='print' for n in ast.walk(f)) for f in functions if f.name!='print_report'))
            stream=io.StringIO()
            with contextlib.redirect_stdout(stream),patch.object(builtins,'input',side_effect=AssertionError('Import must not prompt')):
                mod=load_module(path,'week3_record_check')
            record('Week 3 import has no prompts or printed output',stream.getvalue()=='')
            record('Week 3 calculation returns two correct results',mod.check(87,100)==(13,87.0))
            record('Week 3 default and custom threshold',mod.status_of(95)=='WARNING' and mod.status_of(95,96)=='OK')


def verify_warmups_and_examples():
    for p in ROOT.rglob('warmup/*.py'):
        inputs=['23.7'] if 'input(' in p.read_text() else []
        script(p,inputs)
    fixtures={
        '01_input_and_casting.py':['R-004','23.7','23.7'],
        '01_while_basics.py':['y','n'],
        '02_sentinel_and_running_total.py':['R-1','quit','2','3','done','87','100','120','100','45','100'],
        '02_for_vs_while.py':['R-1','87','100','R-2','120','100','R-3','45','100','R-4','105','100','quit','-1']}
    for p in sorted(ROOT.rglob('examples/*.py')):
        script(p,fixtures.get(p.name,[]))
    example=next(ROOT.rglob('03_main_guard.py'))
    script(example,absent=('checker.py is running directly',))
    script(example.parent/'checker.py',contains=('checker.py is running directly',))
    # Perform the requested temporary edit in a disposable copy of the teaching module.
    with tempfile.TemporaryDirectory() as tmp:
        target=Path(tmp)/'checker.py'
        target.write_text((example.parent/'checker.py').read_text()+'\nprint("temporary unguarded print")\n')
        importer=Path(tmp)/'importer.py'
        importer.write_text('import checker\n')
        script(importer,contains=('temporary unguarded print',),absent=('checker.py is running directly',))


def verify_optional_projects():
    fixtures={
        'band_name.py':(['Lagos','Nova'],('Lagos Nova',)),
        'tip_calculator.py':(['150','5','12'],('$33.60',)),
        'pizza.py':(['S','y','y'],('Your final bill is: $18.',)),
        'treasure_island.py':(['left','wait','yellow'],('You found the treasure!',)),
        'higher_lower.py':(['a','b','quit'],('Correct','Wrong')),
        'rock_paper_scissors.py':(['rock'],('Computer:','Winner:')),
        'calculator.py':(['10','+','5','y','*','2','n','8','/','2','q'],('10.0 + 5.0 = 15.0','15.0 * 2.0 = 30.0','8.0 / 2.0 = 4.0'))}
    for p in ROOT.rglob('EXTRA_PRACTICE/*.py'):
        if p.name=='number_guessing.py':
            if 'import random' in p.read_text():
                with patch('random.randint',return_value=42):
                    out,err,ns,unused=run_code(p.read_text(),['50','30','42'])
                record('Week 3 random guessing with controlled secret',err is None and not unused and 'Too high' in out and 'Too low' in out and '3 guesses' in out)
                record('Week 3 chooses a random secret in 1..100','random.randint(1, 100)' in p.read_text())
            else:
                script(p,['50','30','42'],contains=('Too high','Too low','3 guesses'))
        elif p.name in fixtures:
            inputs,contains=fixtures[p.name]
            script(p,inputs,contains=contains)
    pizza=next(ROOT.rglob('pizza.py'))
    for size,base in [('S',15),('M',20),('L',25)]:
        for pepperoni in ['y','n']:
            for cheese in ['y','n']:
                total=base+(2 if size=='S' else 3)*(pepperoni=='y')+(cheese=='y')
                script(pizza,[size,pepperoni,cheese],contains=(f'Your final bill is: ${total}.',))
    game=load_module(next(ROOT.rglob('rock_paper_scissors.py')),'rps')
    expected={('rock','rock'):'draw',('rock','paper'):'computer',('rock','scissors'):'user',('paper','rock'):'user',('paper','paper'):'draw',('paper','scissors'):'computer',('scissors','rock'):'computer',('scissors','paper'):'user',('scissors','scissors'):'draw'}
    for choices,winner in expected.items():
        record(f'RPS outcome {choices}',game.decide_winner(*choices)==winner)
    for number,choice in enumerate(['rock','paper','scissors']):
        with patch('random.randint',return_value=number):
            record(f'RPS computer choice {number}',game.get_computer_choice()==choice)
    calculator=next(ROOT.rglob('calculator.py'))
    script(calculator,['10','/','0','+','2','q'],contains=('Cannot divide by zero','10.0 + 2.0 = 12.0'))
    script(calculator,['10','?','q'],contains=('Unknown operator.',))


def main():
    run_notebooks()
    verify_semantics()
    verify_projects()
    verify_warmups_and_examples()
    verify_optional_projects()
    from verify_week4 import verify_week4
    verify_week4(sys.modules[__name__])
    failures=[r for r in RESULTS if not r['passed']]
    report={'verified_at_utc':datetime.now(timezone.utc).isoformat(),
            'python_version':sys.version.split()[0],
            **STATS,'checks':len(RESULTS),'passed':len(RESULTS)-len(failures),
            'failed':len(failures),'results':RESULTS,
            'limits':['Verifies worked code, not student understanding.',
                      'Intentional errors are expected and recorded.',
                      'Normal mini-project runs assume numeric inputs and positive totals.',
                      'CW1 brief reviewed; final Moodle deadline, submission and receipt remain unconfirmed.',
                      'Week 4 handwritten photos are present, but topic coverage and cumulative-sheet layout remain incomplete.',
                      'Independent understanding checks remain in progress.']}
    evidence=ROOT/'evidence'
    evidence.mkdir(exist_ok=True)
    (evidence/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    transcript = 'AUTOMATED SAMPLE RUNS — not a personal learning journal.\nTrailing spaces trimmed for readability; inputs are listed separately.\n\n' + '\n\n'.join(TRANSCRIPTS)
    (evidence/'sample_runs.txt').write_text('\n'.join(line.rstrip() for line in transcript.splitlines()) + '\n')
    print(f'{len(RESULTS)-len(failures)}/{len(RESULTS)} checks passed; {STATS["notebooks"]} notebooks, {STATS["code_cells"]} code cells, {STATS["expected_notebook_errors"]} intentional notebook errors.')
    for failure in failures:
        print('FAILED:',failure['check'],failure['details'])
    return 1 if failures else 0


if __name__=='__main__':
    sys.exit(main())
