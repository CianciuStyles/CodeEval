import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		digits = [int(digit) for digit in test.strip() if digit != ' '][::-1]
		odd_digits = digits[::2]
		even_digits = [2 * digit for digit in digits[1::2]]
		sum_even_digits = 0
		for even_digit in even_digits:
			if even_digit < 10:
				sum_even_digits += even_digit
			else:
				sum_even_digits += even_digit % 10 + even_digit // 10
		checksum = sum(odd_digits) + sum_even_digits
		
		print('1' if checksum % 10 == 0 else '0')