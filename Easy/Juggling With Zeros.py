import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        zero_based_number = test.strip().split(' ')
        binary = ''
        for i in range(0, len(zero_based_number), 2):
            flag = zero_based_number[i]
            sequence = zero_based_number[i+1]

            if flag == '0':
                binary += sequence
            elif flag == '00':
                binary += '1' * len(sequence)
            else:
                pass

        print(int(binary, 2))