import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        cities = test.strip().split(';')
        cities = [couple.strip().split(',') for couple in cities[:-1]]
        cities = list(map(lambda x: (x[0], int(x[1])), cities))

        result, last_distance = [], 0
        for city, distance in sorted(cities, key=lambda x: x[1]):
            result.append(distance - last_distance)
            last_distance = distance

        print(','.join(list(map(str, result))))