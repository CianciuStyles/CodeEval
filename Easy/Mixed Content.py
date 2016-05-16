import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        mixed = test.strip().split(',')
        words = list(filter(lambda word: word.isalpha(), mixed))
        digits = list(filter(lambda digit: digit.isdigit(), mixed))

        if len(words) == 0 or len(digits) == 0:
            print(test.strip())
        else:
            print('|'.join([','.join(words), ','.join(digits)]))
