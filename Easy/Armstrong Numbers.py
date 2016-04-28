import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		N = test.strip()
		print(int(N) == sum([int(digit) ** len(N) for digit in N]))