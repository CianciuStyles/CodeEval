import itertools
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		words = test.strip().split(' ')
		print(' '.join([word[0].upper() + word[1:] for word in words]))