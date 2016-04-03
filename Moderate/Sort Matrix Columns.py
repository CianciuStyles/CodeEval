import sys

def transpose(matrix):
	new_matrix = []

	for col in range(len(matrix[0])):
		line = []
		for row in range(len(matrix)):
			line.append(matrix[row][col])

		new_matrix.append(line)

	return new_matrix

def less(col1, col2):
	for index in len(col1):
		compare = col1[index] - col2[index]
		if compare != 0:
			return compare

	return 0

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		rows = test.strip().split(' | ')
		matrix = []
		for row in rows:
			matrix.append([int(digit) for digit in row.split(' ')])
		# print(matrix)

		matrix = transpose(sorted(transpose(matrix)))
		# print(matrix)

		rows = []
		for row in matrix:
			current_row = [str(digit) for digit in row]
			rows.append(" ".join(current_row))

		print(" | ".join(rows))