import sys

with open(sys.argv[1], 'r') as test_cases:
	total = 0
	for test in test_cases:
		total += int(test.strip())

	print(total)