import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        age = int(test.strip())
        if age < 0 or age > 100:
            print('This program is for humans')
        elif age <= 2:
            print('Still in Mama\'s arms')
        elif age <= 4:
            print('Preschool Maniac')
        elif age <= 11:
            print('Elementary school')
        elif age <= 14:
            print('Middle school')
        elif age <= 18:
            print('High school')
        elif age <= 22:
            print('College')
        elif age <= 65:
            print('Working for the man')
        else:
            print('The Golden Years')