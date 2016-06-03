import sys


def create_submatrix(matrix, N, start_x, start_y):
    submatrix = []
    for row in range(start_x, start_x + N):
        new_row = []

        for col in range(start_y, start_y + N):
            new_row.append(matrix[row][col])

        submatrix.append(new_row)
    return submatrix


def count_black_squares(matrix):
    result = 0
    for row in matrix:
        for el in row:
            result += 1 if el == '1' else 0

    return result


def search_other_submatrix(matrix, submatrix, N):
    found = True

    for row in range(0, len(matrix) - N + 1):
        for col in range(0, len(matrix) - N + 1):
            other_submatrix = create_submatrix(matrix, N, row, col)

            if count_black_squares(submatrix) != count_black_squares(other_submatrix):
                found = False

    return (N, count_black_squares(submatrix)) if found else (-1, -1)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        rows = test.strip().split(' | ')
        matrix = []
        for row in rows:
            matrix.append(list(row))

        for N in range(1, len(matrix)+1):
            submatrix = create_submatrix(matrix, N, 0, 0)

            dimension, num_squares = search_other_submatrix(matrix, submatrix, N)
            if dimension != -1:
                break

        if dimension == -1:
            print('{0}x{0}, {1}'.format(N, count_black_squares(matrix)))
        else:
            print('{0}x{0}, {1}'.format(dimension, num_squares))