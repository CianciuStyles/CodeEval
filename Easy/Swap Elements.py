import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		components = test.strip().split(' : ')
		numbers, swaps = components[0].split(' '), components[1].split(', ')
		
		for swap in swaps:
			indices = [int(index) for index in swap.split('-')]

			temp = numbers[indices[0]]
			numbers[indices[0]] = numbers[indices[1]]
			numbers[indices[1]] = temp

		print(' '.join(numbers))