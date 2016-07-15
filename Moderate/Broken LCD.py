import sys

numbers_to_binary = {
	'0': '11111100',
	'1': '01100000',
	'2': '11011010',
	'3': '11110010',
	'4': '01100110',
	'5': '10110110',
	'6': '10111110',
	'7': '11100000',
	'8': '11111110',
	'9': '11110110',
	'.': '00000001'
}

def can_display(digits, numbers):
	for index, number in enumerate(numbers):
		if int(digits[index], 2) & number != number:
			return False

	return True


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	if test == '':
    		continue

    	digits, number = test.strip().split(';')
    	digits = digits.split(' ')

    	#print(digits)
    	#print(number)

    	lcd_numbers = [int(numbers_to_binary[digit], 2) for digit in number]
    	#print(lcd_numbers)

		decimal_index = number.index('.')
		#print(decimal_index)

		lcd_numbers[decimal_index-1] |= 1
		del lcd_numbers[decimal_index]

    	#print(lcd_numbers)

    	can_be_displayed = False
    	for index in range(len(digits)-len(lcd_numbers)+1):
    		current_digits = digits[index:index + len(lcd_numbers)]
    		can_be_displayed = can_display(current_digits, lcd_numbers)
    		if can_be_displayed is True:
    			print('1')
    			break
    	else:
    		print('0')
