import re
import sys

with open(sys.argv[1], 'r') as test_cases:
	word_regex = re.compile(r'[A-Za-z]+')

	for test in test_cases:
		if test == '':
			continue
			
		words = [word.lower() for word in re.findall(word_regex, test.strip())]
		print(' '.join(words))
