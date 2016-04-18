import sys

def generate_column_names():
	letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	names = []

	for letter in letters:
		names.append(letter)

	for letter in letters:
		for second in letters:
			names.append(letter + second)

	for letter in letters:
		for second in letters:
			for third in letters:
				names.append(letter + second + third)

	return names

with open(sys.argv[1], 'r') as test_cases:
	column_names = generate_column_names()

	for test in test_cases:
		if test == "":
			continue

		column_number = int(test.strip())
		print(column_names[column_number - 1])