import math
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		o, p, q, r = [int(point) for point in test.strip().split(' ')]

		dx, dy = q - o, r - p

		if dx > 0:
			if dy > 0:
				print('NE')
			elif dy < 0:
				print('SE')
			else: # dy == 0
				print('E')
		elif dx < 0:
			if dy > 0:
				print('NW')
			elif dy < 0:
				print('SW')
			else: # dy == 0
				print('W')
		else: # dx == 0
			if dy > 0:
				print('N')
			elif dy < 0:
				print('S')
			else: # dy == 0
				print('here')