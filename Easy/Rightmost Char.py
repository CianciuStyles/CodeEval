import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		string, char = test.strip().split(',')
		print(str(string.rfind(char)))