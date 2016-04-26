import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		list_1, list_2 = [sublist.split(' ') for sublist in test.strip().split(' | ')]
		result_list = [int(ziplist[0]) * int(ziplist[1]) for ziplist in zip(list_1, list_2)]
		print(' '.join([str(result) for result in result_list]))