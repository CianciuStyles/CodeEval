import math
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		points = test.strip().split(' ')

		x_A = int(points[0][1:-1])
		y_A = int(points[1][:-1])

		x_B = int(points[2][1:-1])
		y_B = int(points[3][:-1])

		distance = int(math.sqrt((x_B - x_A) ** 2 + (y_B - y_A) ** 2))
		print(distance)