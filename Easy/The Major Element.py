import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		frequencies = collections.defaultdict(int)
		numbers = [int(number) for number in test.split(',')]

		for num in numbers:
			frequencies[num] += 1

		max_num, max_freq = 0, 0
		for num, freq in frequencies.items():
			if freq > max_freq:
				max_num, max_freq = num, freq

		if max_freq > len(numbers) / 2:
			print(max_num)
		else:
			print('None')