import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        number_of_zeros, upper_limit = list(map(int, test.strip().split(' ')))
        total = len([bin(number) for number in range(1, upper_limit+1) if bin(number)[2:].count('0') == number_of_zeros])
        print(total)