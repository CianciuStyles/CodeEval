import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		unique_numbers = []
		unique_numbers = [integer for integer in test.strip().split(',') if integer not in unique_numbers and not unique_numbers.append(integer)]
		print(','.join(unique_numbers))