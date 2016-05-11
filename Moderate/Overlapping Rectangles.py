import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		coords = list(map(int, test.strip().split(',')))
		upperLeftA  = {'x': coords[0], 'y': coords[1]}
		lowerRightA = {'x': coords[2], 'y': coords[3]}
		upperLeftB  = {'x': coords[4], 'y': coords[5]}
		lowerRightB = {'x': coords[6], 'y': coords[7]}

		if (lowerRightA['y'] > upperLeftB['y'] or
			upperLeftA['y'] < lowerRightB['y'] or
			lowerRightA['x'] < upperLeftB['x'] or
			upperLeftA['x'] > lowerRightB['x']):
			print('False')
		else:
			print('True')