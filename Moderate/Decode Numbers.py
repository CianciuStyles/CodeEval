import sys

def number_of_decoded_ways(encoded_message):
	if not encoded_message or len(encoded_message) == 1:
		return 1

	chars, result = 1, 0
	while True:
		target = encoded_message[:chars]
		if len(target) != chars or int(target) > 26:
			break

		result += number_of_decoded_ways(encoded_message[chars:])
		chars += 1

	return result

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		encoded_message = test.strip()
		print(number_of_decoded_ways(encoded_message))