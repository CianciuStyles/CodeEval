import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		print(str(sum([int(digit) for digit in test.strip()])))