import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		S, result = test.strip().split(' '), ''
		for index, elem in enumerate(S):
			if index == 0:
				last_elem, run_length = elem, 1
				continue

			if elem != last_elem:
				result += '{} {} '.format(run_length, last_elem)
				last_elem, run_length = elem, 0

			run_length += 1

		result += '{} {} '.format(run_length, last_elem)
		print(result)