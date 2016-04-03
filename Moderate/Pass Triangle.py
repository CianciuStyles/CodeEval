import sys

with open(sys.argv[1], 'r') as test_cases:
	triangle = []
	for test in test_cases:
		if test == '':
			continue

		row = [int(digit) for digit in test.strip().split(' ')]
		triangle.append(row)

	for row in range(len(triangle)-2, -1, -1):
		for col in range(len(triangle[row])):
			triangle[row][col] += max([triangle[row+1][col], triangle[row+1][col+1]])

	print(triangle[0][0])
