import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		result = ''
		for char in test.strip():
			if char.isdigit():
				result += char
			elif char == 'a':
				result += '0'
			elif char == 'b':
				result += '1'
			elif char == 'c':
				result += '2'
			elif char == 'd':
				result += '3'
			elif char == 'e':
				result += '4'
			elif char == 'f':
				result += '5'
			elif char == 'g':
				result += '6'
			elif char == 'h':
				result += '7'
			elif char == 'i':
				result += '8'
			elif char == 'j':
				result += '9'

		print('NONE' if result == '' else result)