import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		string = test.strip()
		result = ''
		for char in string:
			if char.isalpha() is True:
				if char.islower():
					result += char.upper()
				else:
					result += char.lower()
			else:
				result += char

		print(result)