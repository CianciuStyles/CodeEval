import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		roman_numeral, number = '', int(test.strip())

		while number > 0:
			if number >= 1000:
				roman_numeral += 'M'
				number -= 1000			
			elif number // 100 == 9:
				roman_numeral += 'CM'
				number -= 900
			elif number >= 500:
				roman_numeral += 'D'
				number -= 500
			elif number // 100 == 4:
				roman_numeral += 'CD'
				number -= 400
			elif number >= 100:
				roman_numeral += 'C'
				number -= 100
			elif number // 10 == 9:
				roman_numeral += 'XC'
				number -= 90
			elif number >= 50:
				roman_numeral += 'L'
				number -= 50
			elif number // 10 == 4:
				roman_numeral += 'XL'
				number -= 40
			elif number >= 10:
				roman_numeral += 'X'
				number -= 10
			elif number % 10 == 9:
				roman_numeral += 'IX'
				number -= 9
			elif number >= 5:
				roman_numeral += 'V'
				number -= 5
			elif number % 10 == 4:
				roman_numeral += 'IV'
				number -= 4
			else:
				roman_numeral += 'I'
				number -= 1

		print(roman_numeral)