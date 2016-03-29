import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		stack = test.strip().split(" ")
		print(" ".join(stack[::-2]))