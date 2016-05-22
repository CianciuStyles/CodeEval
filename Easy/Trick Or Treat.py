import math
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        components = test.strip().split(', ')
        vampires, zombies, witches, houses = [int(component.split(':')[1]) for component in components]

        total_candles = (3 * vampires + 4 * zombies + 5 * witches) * houses
        candles_for_each_child = int(math.floor(total_candles // (vampires + zombies + witches)))
        print(candles_for_each_child)