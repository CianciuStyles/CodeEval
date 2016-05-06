import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		number, self_describing = test.strip(), True
		for i in range(len(number)):
			if int(number[i]) != number.count(str(i)):
				self_describing = False

		print('1' if self_describing else '0')