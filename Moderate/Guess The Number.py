import math
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		game = test.strip().split(' ')
		lower, higher = 0, int(game[0])

		for command in game[1:]:
			curr = lower + math.ceil((higher - lower) / 2)

			if command == 'Yay!':
				break
			elif command == 'Lower':
				higher = curr - 1
			elif command == 'Higher':
				lower = curr + 1

		print(curr)