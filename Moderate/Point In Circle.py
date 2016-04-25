import math
import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		components = test.strip().split('; ')

		center = components[0][components[0].find('(')+1:components[0].find(')')]
		center_x, center_y = [float(coord) for coord in center.split(', ')]
		
		radius = float(components[1].split(': ')[1])

		point = components[2][components[2].find('(')+1:components[2].find(')')]
		point_x, point_y = [float(coord) for coord in point.split(', ')]

		distance = math.sqrt((center_x - point_x) ** 2 + (center_y - point_y) ** 2)

		print('true' if distance < radius else 'false')