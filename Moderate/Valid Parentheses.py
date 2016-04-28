import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		S = test.strip()
		if len(S) % 2 == 1:
			print('False')
			continue

		open_pars = []
		result = True
		for char in test.strip():
			if char == '(' or char == '[' or char == '{':
				open_pars.append(char)
			else:
				try:
					last_open = open_pars.pop()
					if (char == ')' and last_open != '(' or
						char == ']' and last_open != '[' or
						char == '}' and last_open != '{'):
						result = False
						break
				except IndexError:
					result = False
					break

		print(result)