import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		text = test.strip()
		if len(text) <= 55:
			print(text)
		else:
			text = text[:40]
			index = text.rfind(' ')
			if index != -1:
				text = text[:index]
			print(text + "... <Read More>")