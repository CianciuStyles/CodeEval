import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		print(bin(int(test.strip())).count('1'))