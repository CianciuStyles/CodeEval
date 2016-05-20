import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        numbers = list(map(int, test.strip().split(' ')))
        street_addresses = sorted(numbers[1:])

        min_distance = float('inf')
        for address in range(street_addresses[0], street_addresses[-1]):
            distance = sum([abs(street_address - address) for street_address in street_addresses])

            if distance < min_distance:
                min_distance = distance

        print(min_distance)