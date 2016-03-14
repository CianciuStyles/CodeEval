import re
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		contents = test.split(', ')
		original_string, forbidden_chars = contents[0], contents[1]
		scrubbed_string = re.sub(r'[{}]'.format(forbidden_chars), '', original_string)
		print(scrubbed_string)