import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		contents = test.strip().split(' ')
		sequence, M = contents[:-1], int(contents[-1])

		if M > len(sequence):
			continue

		print(sequence[-M])