import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '' or test == '\n':
			continue

		components = test.strip().split('|')
		ciphertext = components[0]
		keys = [int(key) for key in components[1].split(' ') if key != '']

		name = ''
		for key in keys:
			name += ciphertext[key-1]

		print(name)