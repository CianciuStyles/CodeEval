import sys

def is_palindrome(num):
	return str(num) == str(num)[::-1]

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		iterations = 0
		while is_palindrome(test) is False:
			test = int(test) + int(str(test)[::-1])
			iterations += 1

		print("{} {}".format(iterations, test))