import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		value = int(test.strip())
		coins = 0
		while value > 0:
			if value >= 5:
				coins += 1
				value -= 5
			elif value >= 3:
				coins += 1
				value -= 3
			elif value >= 1:
				coins += 1
				value -=1

		print(coins)