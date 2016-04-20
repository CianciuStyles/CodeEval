import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		components = test.strip().split(';')
		array = [int(number) for number in components[1].split(',')]
		duplicate = [number for number in array if array.count(number) == 2]
		print(duplicate[0])