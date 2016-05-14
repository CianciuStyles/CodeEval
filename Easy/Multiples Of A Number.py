import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		x, n = list(map(int, test.strip().split(',')))
		m = n

		while x > m:
			m += n

		print(m)