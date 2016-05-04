import math
import sys

with open(sys.argv[1], 'r') as test_cases:
	roman = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}

	for test in test_cases:
		if test == '':
			continue

		number = test.strip()
		total = 0

		for index in range(0, len(number), 2):
			pair = number[index:index+2]
			value = int(pair[0]) * roman[pair[1]]
			
			try:
				consecutive_pair = number[index+2:index+4]
				if roman[consecutive_pair[1]] > roman[pair[1]]:
					total -= value
				else:
					total += value
			except:
				total += value

		print(total)