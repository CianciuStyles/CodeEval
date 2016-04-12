import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		alphabet = list('abcdefghijklmnopqrstuvwxyz')
		for letter in test.strip():
			try:
				alphabet.remove(letter.lower())
			except ValueError:
				continue

		print(''.join(alphabet) if len(alphabet) > 0 else 'NULL')