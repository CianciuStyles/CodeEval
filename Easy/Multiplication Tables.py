for a in range(1, 13):
    line = ''

    for b in range(1, 13):
        line += '{0: >4}'.format(a*b)

    print(line)
