import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		sets = [myset.split(',') for myset in test.strip().split(';')]

		intersection = [val for val in sets[0] if val in sets[1]]
		print(','.join(intersection))