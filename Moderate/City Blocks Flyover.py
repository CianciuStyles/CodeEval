import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        streets, avenues = list(map(lambda s: s[1:-1], test.strip().split(' ')))
        streets = list(map(int, streets.split(',')))
        avenues = list(map(int, avenues.split(',')))
        slope = avenues[-1] / streets[-1] if streets[-1] != 0 else float('inf')

        count = 0
        for i, left in enumerate(streets):
            try:
                right = streets[i+1]
            except IndexError:
                continue

            for j, bottom in enumerate(avenues):
                try:
                    top = avenues[j+1]
                except IndexError:
                    continue

                slope_to_top_left = top / left if left != 0 else float('inf')
                slope_to_bottom_right = bottom / right if right != 0 else float('inf')

                if slope < slope_to_top_left and slope > slope_to_bottom_right:
                    count += 1

        print(count)
