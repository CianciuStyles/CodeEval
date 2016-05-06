import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		number, S = test.strip().split(' ')

		try:
			op_index, add = S.index('+'), True
		except ValueError:
			op_index, add = S.index('-'), False

		first_add, second_add = int(number[:op_index]), int(number[op_index:])
		print(first_add + second_add if add else first_add - second_add)