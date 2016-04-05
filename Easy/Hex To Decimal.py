import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		decimal = int(test.strip(), 16)
		print(str(decimal))