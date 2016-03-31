import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		if len(test) > 55:
			test = test.strip()[:41]
			test = test[:test.rfind(" ")]
			print("{}... <Read More>".format(test))
		else:
			print(test.strip())