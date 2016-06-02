import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		numbers = list(map(int, test.strip().split(',')))
		result = 0

		for i1 in range(len(numbers)-3):
			for i2 in range(i1+1, len(numbers)-2):
				for i3 in range(i2+1, len(numbers)-1):
					for i4 in range(i3+1, len(numbers)):
						if numbers[i1] + numbers[i2] + numbers[i3] + numbers[i4] == 0:
							result += 1

		print(result)