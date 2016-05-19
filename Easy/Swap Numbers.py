import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        words = test.strip().split(' ')
        new_words = []
        for word in words:
            new_words.append(word[-1] + word[1:-1] + word[0])

        print(' '.join(new_words))