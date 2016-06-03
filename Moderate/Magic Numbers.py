import sys


def is_magic(number):
    for digit in number:
        if number.count(digit) > 1:
            return False

    position, visited = 0, [False] * len(number)
    while visited[position] is False:
        visited[position] = True
        current = ord(number[position]) - ord('0')
        position = (position + current) % len(number)

    return position == 0 and visited.count(False) == 0

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        A, B = list(map(int, test.strip().split(' ')))
        magic_numbers = []
        for number in range(A, B+1):
            str_number = str(number)
            if is_magic(str_number):
                magic_numbers.append(str_number)

        print('-1' if len(magic_numbers) == 0 else ' '.join(magic_numbers))