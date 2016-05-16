import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        number, p1, p2 = list(map(int, test.strip().split(',')))
        bin_number = bin(number)[2:]
        print('true' if bin_number[-p1] == bin_number[-p2] else 'false')
