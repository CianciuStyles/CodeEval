import functools
import re
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		regex = re.compile(r'(.+ .+)( \1)+')
		match = regex.search(test.strip())
		cycle = functools.reduce(lambda r, v: v in r and r or r + [v], match.group(1).split(' '), [])
		print(' '.join(cycle))