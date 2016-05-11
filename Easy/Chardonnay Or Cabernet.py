import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		wines, pattern = test.strip().split(' | ')
		wines = wines.split(' ')

		result = []
		for wine in wines:
			n_pattern = list(pattern)
			n_wine = list(wine.lower())
			
			for char in n_wine:
				try:
					n_pattern.remove(char)
				except:
					pass

			if len(n_pattern) == 0:
				result.append(wine)

		print('False' if len(result) == 0 else ' '.join(result))