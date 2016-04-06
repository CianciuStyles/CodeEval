import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		components = test.strip().split(' | ')
		viruses = [int(virus, 16) for virus in components[0].split(' ')]
		antiviruses = [int(antivirus, 2) for antivirus in components[1].split(' ')]

		print(sum(viruses) <= sum(antiviruses))