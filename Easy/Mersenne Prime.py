import sys

mersenne_numbers = [3, 7, 31, 127, 2047]

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		less_than_test = list(map(str, filter(lambda x: x < int(test), mersenne_numbers)))
		print(', '.join(less_than_test))