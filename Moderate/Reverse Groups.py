import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		components = test.strip().split(';')
		k = int(components[1])
		numbers = components[0].split(',')

		reversed_numbers, i = [], 0
		while i < len(numbers):
			if i + k <= len(numbers):
				nums = reversed(numbers[i:i+k])
			else:
				nums = numbers[i:]

			reversed_numbers += nums
			i += k

		print(','.join(reversed_numbers))