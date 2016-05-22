import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        number = test.strip()
        numbers_seen_so_far, happy = [], False

        while number not in numbers_seen_so_far:
            numbers_seen_so_far.append(number)
            square_digits = list(map(lambda x: int(x) ** 2, number))
            number = str(sum(square_digits))
            if number == '1':
                happy = True
                break

        print('1' if happy is True else '0')