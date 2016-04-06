import itertools
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		perms = set([''.join(p) for p in itertools.permutations(test.strip())])
		print(','.join(sorted(perms)))