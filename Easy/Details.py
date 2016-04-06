import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		lines = test.strip().split(',')
		min_movement = float('inf')
		for line in lines:
			first_y = line.find('Y')
			last_x = line.rfind('X')

			min_movement = min(min_movement, first_y - last_x - 1)

		print(min_movement)