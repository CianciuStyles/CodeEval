import itertools
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		beauty = 0

		chars = sorted([char.lower() for char in test if char.isalpha()])
		# print(chars)

		chars_frequency_dict = {key: len(list(group)) for key, group in itertools.groupby(chars)}
		char_groups = sorted(chars_frequency_dict.items(), key=lambda pair: pair[1], reverse=True)
		for index, (key, size) in enumerate(char_groups):
			# print("{} {}".format(key, size))
			beauty += (26-index) * size

		print("{}".format(beauty))