import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		N, M = list(map(int, test.split(',')))
		while N >= M:
			N -= M

		print(N)