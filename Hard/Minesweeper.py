import sys

def generate_minefield(m, n, string):
	minefield = []
	for i in range(m):
		row = string[n*i:n*i+n]
		minefield.append([char for char in row])

	return minefield

def check_neighbours(minefield, i, j):
	if minefield[i][j] == '*':
		return '*'

	num_mines = 0
	for n_i in range(i-1, i+2):
		if n_i < 0 or n_i > len(minefield) - 1:
			continue

		for n_j in range(j-1, j+2):
			if n_i == i and n_j == j:
				continue

			if n_j < 0 or n_j > len(minefield[n_i])-1:
				continue

			if minefield[n_i][n_j] == '*':
				num_mines += 1

	return str(num_mines)

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		components = test.strip().split(';')
		rows_and_cols = [int(comp) for comp in components[0].split(',')]
		M, N = rows_and_cols[0], rows_and_cols[1]
		minefield = generate_minefield(M, N, components[1])

		result = ''
		for i in range(M):
			for j in range(N):
				result += check_neighbours(minefield, i, j)

		print(result)