import functools
import re
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		limit = int(test.strip())
		if limit == 1:
			print('1')
			continue
		elif limit == 2:
			print('1 1 1')
			continue
		else:
			triangle = [[1], [1, 1]]
			for row in range(2, limit):
				new_line = [1]
				for i in range(len(triangle[row-1]) - 1):
					new_line.append(triangle[row-1][i] + triangle[row-1][i+1])
				new_line.append(1)
				triangle.append(new_line)

		digits = [str(digit) for digit in sum(triangle, [])]
		print(' '.join(digits))