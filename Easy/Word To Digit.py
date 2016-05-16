import sys

word_to_digit = {
    'zero': '0', 'one': '1', 'two': '2',
    'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        words = test.strip().split(';')
        digits = [word_to_digit[word] for word in words]
        print(''.join(digits))
