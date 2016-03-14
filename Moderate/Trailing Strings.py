import re
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		contents = test.split(',')
		string_A, string_B = contents[0].strip(), contents[1].strip()
		
		if string_A.endswith(string_B) is True:
			print("1")
		else:
			print("0")