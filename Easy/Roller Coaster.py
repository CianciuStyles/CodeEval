import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		upper = True
		S = test.strip()
		result = ''
		for char in S:
			if char.isalpha():
				result += char.upper() if upper is True else char.lower()
				upper = not upper
			else:
				result += char

		print(result)