import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		S = test.strip()
		period_length = S[1:].find(S[0])
		if period_length != -1:
			print(period_length + 1)
		else:
			print(len(S))