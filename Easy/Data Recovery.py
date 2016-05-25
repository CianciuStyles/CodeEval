import itertools
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        words, hints = test.strip().split(';')
        words = words.split(' ')
        hints = list(map(int, hints.split(' ')))
        fill = [num for num in range(1, len(words)+1) if num not in hints][0]

        new_words = sorted(itertools.zip_longest(words, hints, fillvalue=fill), key=lambda x: x[1])
        print(' '.join([new_word[0] for new_word in new_words]))