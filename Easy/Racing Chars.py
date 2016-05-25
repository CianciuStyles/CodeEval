import sys

with open(sys.argv[1], 'r') as test_cases:
    board = []

    for test in test_cases:
        if test == '':
            continue

        board.append(test.strip())

    new_board, prev_row_index = [], -1
    for row in board:
        start = row.find('C')
        if start == -1:
            start = row.find('_')

        new_line = row[:start]
        if prev_row_index == -1:
            new_line += '|'
        else:
            if start < prev_row_index:
                new_line += '/'
            elif start > prev_row_index:
                new_line += '\\'
            else:
                new_line += '|'
        prev_row_index = start
        new_line += row[start+1:]
        new_board.append(new_line)

    print('\n'.join(new_board))