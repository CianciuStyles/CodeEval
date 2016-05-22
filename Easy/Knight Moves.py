import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        column, row = list(test.strip())
        column = ord(column) - 97
        row = int(row)

        moves = []
        if column - 2 >= 0:
            if row - 1 >= 1:
                moves.append('%s%d' % (chr(column + 97 - 2), row - 1))
            if row + 1 <= 8:
                moves.append('%s%d' % (chr(column + 97 - 2), row + 1))

        if column - 1 >= 0:
            if row - 2 >= 1:
                moves.append('%s%d' % (chr(column + 97 - 1), row - 2))
            if row + 2 <= 8:
                moves.append('%s%d' % (chr(column + 97 - 1), row + 2))

        if column + 1 <= 7:
            if row - 2 >= 1:
                moves.append('%s%d' % (chr(column + 97 + 1), row - 2))
            if row + 2 <= 8:
                moves.append('%s%d' % (chr(column + 97 + 1), row + 2))

        if column + 2 <= 7:
            if row - 1 >= 1:
                moves.append('%s%d' % (chr(column + 97 + 2), row - 1))
            if row + 1 <= 8:
                moves.append('%s%d' % (chr(column + 97 + 2), row + 1))

        print(' '.join(moves))