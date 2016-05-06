import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		matrix = list(map(list, test.strip().split(' | ')))
		result = 0

		for row in range(len(matrix)-1):
			for col in range(len(matrix[0])-1):
				code = sorted([
					matrix[row][col],
					matrix[row+1][col],
					matrix[row][col+1],
					matrix[row+1][col+1]
					])

				if code == ['c', 'd', 'e', 'o']:
					result +=1

		print(result)