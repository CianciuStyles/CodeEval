import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        array, max_number_of_iterations = test.strip().split(' | ')
        array = list(map(int, array.split(' ')))
        max_number_of_iterations = int(max_number_of_iterations)

        current_number_of_iterations, i = 0, 0
        while True:
            try:
                if array[i] > array[i+1]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
                    current_number_of_iterations += 1
                    if current_number_of_iterations == max_number_of_iterations:
                        break
                    i = 0
                else:
                    i += 1
            except IndexError:
                break

        print(' '.join(list(map(str, array))))