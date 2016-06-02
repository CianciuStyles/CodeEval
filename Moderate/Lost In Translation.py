import sys

input_str = b'ynficwlbkuomxsevzpdrjgthaq'
output_str = b'abcdefghijklmnopqrstuvwxyz'
translation = bytes.maketrans(input_str, output_str)

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		print(test.strip().translate(translation))