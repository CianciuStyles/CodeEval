import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		numbers = [number for number in test.strip().split(' ')]
		numbers = [(number, index+1) for index, number in enumerate(numbers) if numbers.count(number) == 1]

		if len(numbers) == 0:
			print('0')
		else:
			print(min(numbers)[1])