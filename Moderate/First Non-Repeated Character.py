import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        chars = list(test.strip())
        non_repeated_characters = [char for char in chars if chars.count(char) == 1]
        print(non_repeated_characters[0])
