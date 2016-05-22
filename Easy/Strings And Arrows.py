import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        string = test.strip()
        total = 0
        for i in range(len(string) - 4):
            if string[i:i+5] == '<--<<' or string[i:i+5] == '>>-->':
                total += 1

        print(total)