import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        time1, time2 = test.strip().split(' ')
        time1, time2 = max([time1, time2]), min([time1, time2])
        h1, m1, s1 = list(map(int, time1.split(':')))
        h2, m2, s2 = list(map(int, time2.split(':')))

        if s1 >= s2:
            s = s1 - s2
        else:
            m1 -= 1
            s = s1 + 60 - s2

        if m1 >= m2:
            m = m1 - m2
        else:
            h1 -= 1
            m = m1 + 60 - m2

        h = h1 - h2

        print('{:02d}:{:02d}:{:02d}'.format(h, m, s))