import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		n = int(test.strip())

		if n == 0:
			print('0')
		elif n == 1:
			print('1')
		else:
			fib1, fib2 = 0, 1
			while n > 1:
				fib1, fib2 = fib2, fib1 + fib2
				n -= 1
			print(fib2)