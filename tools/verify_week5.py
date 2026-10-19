"""Behaviour checks for Week 5 walkthrough answers; support tooling, not coursework."""
import ast
import json
import math
from pathlib import Path
from unittest.mock import patch


def verify_week5(v):
    week = v.ROOT / 'Week 05 - Classes and Objects'
    check = v.record
    paths = {
        1: week / '01 - Classes and Objects/W05T01_walkthrough.ipynb',
        2: week / '02 - Methods/W05T02_walkthrough.ipynb',
        3: week / '03 - Many Objects Together/W05T03_walkthrough.ipynb',
    }
    notebooks = {number: json.loads(path.read_text()) for number, path in paths.items()}

    def definitions(topic, index):
        source = ''.join(notebooks[topic]['cells'][index]['source'])
        tree = ast.parse(source)
        tree.body = [node for node in tree.body
                     if isinstance(node, (ast.ClassDef, ast.FunctionDef))]
        namespace = {'__name__': 'week5_verification'}
        exec(compile(tree, str(paths[topic]), 'exec'), namespace)
        return namespace

    prompts = 0
    challenges = 0
    complete = True
    for nb in notebooks.values():
        for i, cell in enumerate(nb['cells']):
            source = ''.join(cell['source'])
            if cell['cell_type'] != 'markdown':
                continue
            is_prompt = source.startswith('### Your turn')
            is_challenge = '## Topic ' in source and ' Challenge' in source
            if is_prompt or is_challenge:
                prompts += is_prompt
                challenges += is_challenge
                answer = ''.join(nb['cells'][i + 1]['source']).strip()
                complete = complete and bool(answer) and '# your code here' not in answer
    check('W05 all 11 Your turn tasks and 3 challenges have answers',
          prompts == 11 and challenges == 3 and complete)

    Server = definitions(1, 5)['Server']
    a = Server('a', 40.0, 100.0)
    b = Server('b', 70.0, 200.0)
    check('W05 constructor stores all three server attributes',
          (a.hostname, a.used, a.total) == ('a', 40.0, 100.0))
    a.used = 99.0
    check('W05 separate server instances keep independent numeric attributes',
          b.used == 70.0 and a.used == 99.0)
    Record = definitions(1, 19)['Record']
    first = Record('first', 87, 100)
    second = Record('second', 120, 100)
    first.label = 'changed'
    check('W05 challenge stores separate record labels and numbers',
          second.label == 'second' and second.value == 120 and first.label == 'changed')

    Record = definitions(2, 4)['Record']
    r = Record('survey', 1187.0, 1200.0)
    check('W05 percent returns a computed number for an unfamiliar ratio',
          math.isclose(r.percent(), 1187 / 1200 * 100))
    check('W05 adding percent preserves summary for the following cells',
          r.summary() == 'survey: 1187.0/1200.0')

    Server = definitions(2, 13)['Server']
    Record = definitions(2, 19)['Record']
    for label, Class in [('server', Server), ('record', Record)]:
        for value, expected in [(0, 'OK'), (89.99, 'OK'), (90, 'WARNING'),
                                (99.99, 'WARNING'), (100, 'OVER LIMIT'),
                                (120, 'OVER LIMIT')]:
            item = Class('sample', value, 100)
            check(f'W05 {label} status boundary {value}', item.status() == expected)
        with patch.object(Class, 'percent', return_value=95.0) as percent:
            # A zero limit would fail if status recalculated instead of using percent().
            status = Class('delegation', 1, 0).status()
        check(f'W05 {label} status calls percent exactly once',
              status == 'WARNING' and percent.call_count == 1)
    record = Record('update', 87, 100)
    record.value = 105
    check('W05 methods read the current object attributes after an update',
          record.percent() == 105 and record.status() == 'OVER LIMIT')

    Checker = definitions(2, 17)['Checker']
    a, b = Checker(), Checker()
    a.check(100, 100)
    check('W05 Checker uses its required strict greater-than rule',
          a.over_limit_count == 0)
    a.check(101, 100)
    a.check(87, 100)
    b.check(120, 100)
    check('W05 Checker counts qualifying calls only', a.over_limit_count == 1)
    a.reset()
    check('W05 reset clears only its own checker',
          a.over_limit_count == 0 and b.over_limit_count == 1)
    a.check(150, 100)
    check('W05 a checker still works after reset', a.over_limit_count == 1)

    shared = definitions(3, 11)['Record']
    item = shared('over', 120, 100)
    item.status()
    item.status()
    check('W05 optional shared counter counts calls, including repeat calls',
          shared.over_limit_count == 2)

    namespace = definitions(3, 19)
    Record, load_records = namespace['Record'], namespace['load_records']
    item = Record('equal', 100, 100)
    before = item.__dict__.copy()
    check('W05 list-of-objects challenge includes exactly 100 percent as over limit',
          item.status() == 'OVER LIMIT')
    item.status()
    check('W05 challenge status does not change state on repeated calls',
          item.__dict__ == before)
    with v.execution_workspace(paths[3]) as target, v.working_directory(target.parent):
        records = load_records('datasets.txt')
        check('W05 loader returns three actual Record objects with converted numbers',
              len(records) == 3 and all(isinstance(r, Record)
              and type(r.value) is float and type(r.limit) is float for r in records))
        check('W05 challenge dataset gives two out of three over limit',
              [r.label for r in records] == ['survey_small', 'sensor_batch', 'complete_batch']
              and sum(r.status() == 'OVER LIMIT' for r in records) == 2)
        Path('empty.txt').write_text('')
        check('W05 loader returns an empty list for an empty file',
              load_records('empty.txt') == [])
        Path('one.txt').write_text('last,90.5,100')
        last = load_records('one.txt')
        check('W05 loader accepts a final line without a newline',
              len(last) == 1 and last[0].value == 90.5 and last[0].status() == 'OK')
        try:
            load_records('not_here.txt')
        except FileNotFoundError:
            missing_file_error = True
        else:
            missing_file_error = False
        check('W05 loader surfaces a missing file, as in the supplied example',
              missing_file_error)

        for index, expected in [(5, 'R-001\nR-003'), (9, '1'),
                                (16, 'survey_a OK\nsurvey_b OVER LIMIT\nsurvey_c OK'),
                                (19, '2 of 3 were over limit')]:
            ns = {'__name__': '__main__'}
            output = ''
            error = None
            for cell in notebooks[3]['cells'][:index + 1]:
                if cell['cell_type'] == 'code':
                    output, error, ns, unused = v.run_code(''.join(cell['source']), namespace=ns)
                    if error:
                        break
            check(f'W05 Topic 3 answer cell {index} has the requested output',
                  error is None and output.strip() == expected)
