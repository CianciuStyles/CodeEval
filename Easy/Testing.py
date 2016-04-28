import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		string_1, string_2 = test.strip().split(' | ')
		num_bugs = 0
		for index, char in enumerate(string_1):
			try:
				if string_2[index] != char:
					num_bugs +=1
			except IndexError:
				num_bugs += 1

		if num_bugs == 0:
			print('Done')
		elif num_bugs <= 2:
			print('Low')
		elif num_bugs <= 4:
			print('Medium')
		elif num_bugs <= 6:
			print('High')
		else:
			print('Critical')