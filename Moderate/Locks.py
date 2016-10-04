import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        N, M = list(map(int, test.strip().split(' ')))
        doors = [True] * N

        for iteration in range(M-1):
            for i in range(1, N, 2):
                doors[i] = False

            for i in range(2, N, 3):
                doors[i] = not doors[i]

        doors[-1] = not doors[-1]

        print(sum(doors))
