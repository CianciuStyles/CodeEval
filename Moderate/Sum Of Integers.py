import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		array = list(map(int, test.strip().split(',')))

		max_sum = float('-inf')
		for l in range(1, len(array)+1):
			for i in range(0, len(array)-l+1):
				max_sum = max(max_sum, sum(array[i:i+l]))

		print(max_sum)