"""Week 4 behavioural checks, called by verify_coursework.py; support tooling only."""
import ast
import contextlib
import io
import json
import math
from pathlib import Path
import random
import tempfile
from unittest.mock import patch


def verify_week4(v):
    week = v.ROOT / 'Week 04 - Lists, Dictionaries and Files'
    lab = week / 'LAB'
    project = lab / 'template.py'
    check = v.record

    stream = io.StringIO()
    with contextlib.redirect_stdout(stream), patch('builtins.input', side_effect=AssertionError('Import must not prompt')):
        mod = v.load_module(project, 'week4_record_check')
    check('W04 project imports without running', stream.getvalue() == '')
    tree = ast.parse(project.read_text())
    functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    check('W04 all functions have one-line docstrings', all(ast.get_docstring(n) and '\n' not in ast.get_docstring(n) for n in functions))
    printers = [n.name for n in functions if any(isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id == 'print' for c in ast.walk(n))]
    check('W04 all console printing belongs to print_report', printers == ['print_report'])
    check('W04 no bare except blocks', all(n.type is not None for n in ast.walk(tree) if isinstance(n, ast.ExceptHandler)))

    for value, limit, expected in [(0,100,'OK'), (89.99,100,'OK'), (90,100,'WARNING'),
                                    (99.99,100,'WARNING'), (100,100,'OVER LIMIT'),
                                    (100.01,100,'OVER LIMIT'), (1187,1200,'WARNING')]:
        difference, percent, status = mod.check_record(value, limit)
        check(f'W04 project status boundary {value}/{limit}', status == expected)
        check(f'W04 project numeric results {value}/{limit}',
              math.isclose(difference, value-limit, abs_tol=1e-12) and math.isclose(percent, value/limit*100, abs_tol=1e-12))
    check('W04 custom warning threshold', mod.check_record(95,100,96)[2] == 'OK')
    for value, limit, expected_error in [('bad',100,TypeError),(1,0,ZeroDivisionError)]:
        try:
            mod.check_record(value, limit)
        except expected_error:
            check(f'W04 documented invalid calculation {value}/{limit}', True)
        else:
            check(f'W04 documented invalid calculation {value}/{limit}', False)

    expected_statuses = ['OK','WARNING','WARNING','OVER LIMIT','OVER LIMIT']
    expected_labels = ['survey_small','sensor_batch','survey_2026','complete_batch','extra_rows']
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        input_path = root/'datasets.txt'
        output_path = root/'output.txt'
        input_path.write_bytes((lab/'datasets.txt').read_bytes())
        original = input_path.read_bytes()
        records = mod.load_records(input_path)
        check('W04 loader returns five typed records with no status field',
              len(records) == 5 and all(set(r) == {'label','value','limit'} and type(r['value']) is float and type(r['limit']) is float for r in records))
        output_path.write_text('Old output that must be replaced\n')
        output = io.StringIO()
        with contextlib.redirect_stdout(output), patch.object(mod, 'check_record', wraps=mod.check_record) as checker:
            mod.main(input_path, output_path)
        check('W04 calculate each record exactly once', checker.call_count == 5)
        console = output.getvalue()
        lines = [line.split(':',1)[1].strip() for line in console.splitlines() if line.startswith('  Status')]
        check('W04 printed statuses follow sample data', lines == expected_statuses)
        expected_text = ''.join(f'{label},{status}\n' for label,status in zip(expected_labels,expected_statuses))
        check('W04 result file contains exact label,status records', output_path.read_text() == expected_text)
        check('W04 summary printed once after all reports', console.count('Checked 5 records. 2 were over limit.') == 1 and console.rstrip().endswith('Checked 5 records. 2 were over limit.'))
        check('W04 report formatting and difference direction', '-130.00' in console and '+50.00' in console and '98.92' in console and '104.17' in console)
        check('W04 input file remains unchanged', input_path.read_bytes() == original)
        v.TRANSCRIPTS.append('WEEK 4 NORMAL PROJECT RUN\n'+console+'\nSAVED dataset_results.txt\n'+output_path.read_text())
        for case in ['missing','empty']:
            path = root/f'{case}.txt'
            if case == 'empty': path.write_text('')
            output = io.StringIO()
            with contextlib.redirect_stdout(output): mod.main(path,output_path)
            check(f'W04 {case} input uses zero records', output.getvalue().rstrip().endswith('Checked 0 records. 0 were over limit.') and output_path.read_text() == '')
            if case == 'missing':
                check('W04 missing input explains fallback', 'not found; starting with an empty list' in output.getvalue())
                v.TRANSCRIPTS.append('WEEK 4 MISSING INPUT RUN\n'+output.getvalue().replace(str(path),'missing.txt'))
        input_path.write_text('single,93,100')
        check('W04 loader accepts final line without newline', mod.load_records(input_path) == [{'label':'single','value':93.0,'limit':100.0}])
        for bad in ['wrong,shape\n','label,abc,100\n']:
            input_path.write_text(bad)
            try: mod.load_records(input_path)
            except ValueError: check(f'W04 malformed input is surfaced {bad.strip()}', True)
            else: check(f'W04 malformed input is surfaced {bad.strip()}', False)

    v.script(project, contains=('Checked 5 records. 2 were over limit.',))

    # Compare the lab answers with the supplied expected output, not just execution success.
    notebook = lab/'W04_Lab.ipynb'
    nb = json.loads(notebook.read_text())
    outputs = {}
    namespace = {'__name__':'__main__'}
    with v.execution_workspace(notebook) as target, v.working_directory(target.parent):
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'code':
                out, error, namespace, unused = v.run_code(''.join(cell['source']),namespace=namespace)
                outputs[i] = out.strip()
        expectations = {
            4: 'R-001\nR-003\n3',
            6: '[10, 15, 20, 25]\n[5, 10]\n[20, 25, 30]',
            8: '[99, 20, 30]\n[99, 20, 30, 40]\n[99, 30, 40]\n99\n30\n40',
            10:'3', 12:'R\n1\n001',
            14:'[80, 110, 140, 50]\n[55, 70]',
            17:"R-001\n{'label': 'R-001', 'value': 90.0, 'limit': 100.0, 'status': 'OK'}",
            19:'OK\nNone\nn/a',
            21:'label\nvalue\nlimit\nstatus\nR-001\n90.0\n100.0\nOK\nlabel: R-001\nvalue: 90.0\nlimit: 100.0\nstatus: OK',
            23:"{'srv-01': 87, 'srv-02': 45, 'srv-03': 120}\n120",
            25:'3\nTrue\nFalse', 28:'R-001\nR-002',
            30:'R-001 87.0 100.0\nR-002 120.0 100.0\nR-003 45.0 100.0',
            33:'Not a number: abc\n42.0', 35:'missing.txt not found',
            38:'R-001: OK\nR-002: OVER LIMIT\nR-003: OK',
            41:'R-001: OK\nR-002: OVER LIMIT\nR-003: OK\nnope.txt not found; returning an empty list\n[]',
            43:'R-001,OK\nR-002,OVER LIMIT\nR-003,OK',
        }
        for index, expected in expectations.items():
            check(f'W04 lab cell {index} matches required output', outputs[index] == expected, outputs[index] if outputs[index] != expected else '')
        check('W04 lab C2 actual file contents', Path('results.txt').read_text() == 'R-001,OK\nR-002,OVER LIMIT\nR-003,OK\n')
        check('W04 lab D12 actual file contents', Path('notes.txt').read_text() == 'R-001\nR-002\n')
        d16 = ''.join(nb['cells'][38]['source']).replace('87.0', '100.0')
        out, error, _, _ = v.run_code(d16)
        check('W04 D16 equality is OK under its strict rule', error is None and 'R-001: OK' in out)
        out,error,_,_ = v.run_code('point = (3,7)\npoint[0] = 5')
        check('W04 D4 requested tuple error reproduced', isinstance(error,TypeError))

    # Run optional exercise definitions, then exercise their genuine failure paths.
    extra_path = week/'EXTRA_PRACTICE/W04_Extra_Practice.ipynb'
    extra = json.loads(extra_path.read_text())
    ns = {'__name__':'__main__'}
    with v.execution_workspace(extra_path) as target, v.working_directory(target.parent):
        for cell in extra['cells']:
            if cell['cell_type'] == 'code':
                meta = cell.get('metadata',{}).get('cst1510',{})
                _,_,ns,_ = v.run_code(''.join(cell['source']),meta.get('sample_inputs',[]),namespace=ns)
        stream = io.StringIO()
        with patch('builtins.open', side_effect=PermissionError('simulated permission denial')), contextlib.redirect_stdout(stream):
            result = ns['read_with_messages']('restricted.txt')
        check('W04 PermissionError handler returns empty text with message', result == '' and 'No permission' in stream.getvalue())
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream): valid = ns['safe_load_records_v2']('broken_records.txt')
        check('W04 safer loader skips bad shape and bad numeric value', len(valid) == 2 and [r['label'] for r in valid] == ['R-001','R-003'] and stream.getvalue().count('Skipping a bad line:') == 2)
        check('W04 two-field loader returns typed rents', ns['load_properties']('properties.txt') == [{'name':'Lekki_flat','rent':1400.0},{'name':'Ikeja_flat','rent':1000.0}])

    practice = week/'EXTRA_PRACTICE'
    banker = v.load_module(practice/'banker_roulette.py','banker')
    stream = io.StringIO()
    with patch.object(banker.random,'choice',return_value='Ada'), patch.object(banker.random,'randint',return_value=3), contextlib.redirect_stdout(stream): banker.main()
    check('W04 banker demonstrates both selection methods', stream.getvalue().splitlines() == ['Using choice: Ada','Using an index: Tunde'])
    password = v.load_module(practice/'password_generator.py','password_practice')
    for counts in [(4,2,3),(0,0,0),(0,1,0)]:
        for shuffled in [False,True]:
            random.seed(1510)
            result = password.make_password(*counts, shuffled=shuffled)
            check(f'W04 password requested character counts {counts} shuffled={shuffled}',
                  len(result) == sum(counts) and sum(c.isalpha() for c in result) == counts[0] and sum(c in '!#$%&()*+' for c in result) == counts[1] and sum(c.isdigit() for c in result) == counts[2])
    v.script(practice/'password_generator.py',['bad','-1','4','2','3'],contains=('Enter a whole number.','Enter zero or more.','Easy version:','Shuffled version:'))
    auction = v.load_module(practice/'blind_auction.py','auction')
    check('W04 auction highest bid and tie policy', auction.highest_bid({'Ada':50,'Musa':80,'Zainab':80}) == ('Musa',80))
    v.script(practice/'blind_auction.py',['Ada','50','yes','Musa','80','no'],contains=('Winner: Musa, bid: 80.00',),absent=('Ada, bid:',))
    v.script(practice/'blind_auction.py',['Ada','nan','Ada','50','yes','Ada','Musa','80','no'],contains=('Enter a positive, finite bid.','Enter a new, nonempty name.','Winner: Musa, bid: 80.00'))
    coffee = v.load_module(practice/'coffee_machine.py','coffee')
    resources = {'water':300,'milk':200,'coffee':100}
    original = resources.copy()
    check('W04 resource check is read-only', coffee.has_ingredients(resources,coffee.MENU['latte']['ingredients']) and resources == original)
    coffee.use_ingredients(resources,coffee.MENU['latte']['ingredients'])
    check('W04 paid latte deducts exact ingredients', resources == {'water':100,'milk':50,'coffee':76})
    v.script(practice/'coffee_machine.py',['latte','2','report','latte','3','report','cappuccino','off'],
             contains=('Not enough payment; refunded.','water: 300','Here is your latte. Change: 0.50','water: 100','milk: 50','coffee: 76','Not enough water.','Not enough milk.'))
    v.script(practice/'coffee_machine.py',['unknown','espresso','abc','espresso','nan','report','off'],
             contains=('Unknown drink.','Enter a numeric payment; order cancelled.','Invalid payment; order cancelled.','water: 300','coffee: 100'))

    prompt_count = 0
    answered = 0
    titles_match = True
    for path in week.glob('*/*.ipynb'):
        if path.parent.name in ['LAB','EXTRA_PRACTICE']: continue
        cells = json.loads(path.read_text())['cells']
        topic_number = int(path.parent.name[:2])
        titles_match = titles_match and f'Topic {topic_number}' in ''.join(cells[0]['source'])
        for index,cell in enumerate(cells):
            if '### Your turn' in ''.join(cell.get('source',[])):
                prompt_count += 1
                following = next(c for c in cells[index+1:] if c['cell_type'] == 'code')
                if ast.parse(''.join(following['source'])).body: answered += 1
    check('W04 all 22 Your turn cells contain executable answers', prompt_count == answered == 22)
    check('W04 walkthrough titles match their topic folders', titles_match)
    photo_cell = nb['cells'][47]
    photo_names = [
        'week-01-IMG_6296.jpg', 'week-02-IMG_6297.jpg',
        'week-02-03-IMG_6298.jpg', 'week-03-IMG_6299.jpg',
        'week-04-lists-IMG_6300.jpg', 'week-04-dictionaries-IMG_6301.jpg',
    ]
    photo_source = ''.join(photo_cell['source'])
    check('W04 supplied photos are embedded in order with remaining coverage pending',
          set(photo_cell.get('attachments', {})) == set(photo_names)
          and all('attachment:' + name in photo_source for name in photo_names)
          and [photo_source.index('attachment:' + name) for name in photo_names]
              == sorted(photo_source.index('attachment:' + name) for name in photo_names)
          and 'Pending:' in photo_source)
