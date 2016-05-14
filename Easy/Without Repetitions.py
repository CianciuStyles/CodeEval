import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		text = test.strip()
		result = ''
		for index, char in enumerate(text):
			if index == 0:
				result += char
				continue

			if char == text[index-1]:
				continue
			else:
				result += char

		print(result)