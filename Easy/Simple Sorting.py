import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        numbers = list(map(float, test.strip().split(' ')))
        result = ''
        for number in sorted(numbers):
            result += '{:.3f} '.format(number)

        print(result[:-1])