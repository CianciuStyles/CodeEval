import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		S = test.strip()
		lowercase, uppercase = 0, 0

		for char in S:
			if char.islower():
				lowercase += 1
			else:
				uppercase += 1

		lowercase = (lowercase / len(S)) * 100
		uppercase = (uppercase / len(S)) * 100

		print('lowercase: {0:.2f} uppercase: {1:.2f}'.format(lowercase, uppercase))