import sys


def compose(substring, mapping):
    if substring == '':
        return ['']

    substrings = compose(substring[1:], mapping)
    result = []
    for char in mapping[substring[0]]:
        for substr in substrings:
            result.append(char + substr)

    return result

with open(sys.argv[1], 'r') as test_cases:
    mapping = {
        '0': ['0'],
        '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    for test in test_cases:
        if test == '':
            continue

        print(','.join(compose(test.strip(), mapping)))
