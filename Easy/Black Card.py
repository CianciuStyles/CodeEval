import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		components = test.strip().split(' | ')
		people, number = components[0].split(' '), int(components[1]) - 1
		while len(people) > 1:
			del people[number % len(people)]

		print(people[0])