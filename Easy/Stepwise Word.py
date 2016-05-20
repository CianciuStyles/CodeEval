import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        words = test.strip().split(' ')
        longest_word = max(words, key=len)
        result = ''
        for index, char in enumerate(longest_word):
            result += index * '*' + char + ' '

        print(result[:-1])