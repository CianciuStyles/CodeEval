import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        string, mask = test.strip().split(' ')
        result = ''
        for index, value in enumerate(mask):
            if value == '1':
                result += string[index].upper()
            else:
                result += string[index].lower()

        print(result)