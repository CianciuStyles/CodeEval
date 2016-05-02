import math
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		S = test.strip().split(' ')
		N = int(math.sqrt(len(S)))

		old_matrix = []
		for row in range(N):
			old_matrix.append(S[row*N:(row+1)*N])

		new_matrix = []
		for col in range(N):
			line = []
			for row in range(N):
				line.insert(0, old_matrix[row][col])
			new_matrix.append(line)

		print(' '.join(sum(new_matrix, [])))