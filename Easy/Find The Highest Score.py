import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        rows = test.strip().split(' | ')
        rows = [list(map(int, row.split(' '))) for row in rows]

        cols = zip(*rows)
        max_in_cols = map(str, map(max, cols))
        print(' '.join(max_in_cols))