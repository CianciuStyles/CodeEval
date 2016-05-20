import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        number_of_days, gains = test.strip().split(';')
        number_of_days = int(number_of_days)
        gains = list(map(int, gains.split(' ')))

        max_gain = 0
        for i in range(len(gains) - number_of_days + 1):
            current_range = gains[i:i+number_of_days]
            current_gain = sum(current_range)
            max_gain = max(current_gain, max_gain)

        print(max_gain)