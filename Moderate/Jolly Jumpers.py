import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		contents = [int(content) for content in test.strip().split(' ')]
		N, sequence = contents[0], contents[1:]

		range_N = list(range(1, N))
		for index in range(1, len(sequence)):
			jump = abs(sequence[index] - sequence[index-1])
			if jump in range_N:
				range_N.remove(jump)

		if not range_N:
			print("Jolly")
		else:
			print("Not jolly")