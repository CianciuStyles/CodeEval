import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		print('1' if int(test) % 2 == 0 else '0')