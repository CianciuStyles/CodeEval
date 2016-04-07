import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		dictionary = collections.defaultdict(list)
		countries = test.strip().split(' | ')
		for index, country in enumerate(countries):
			teams = country.split(' ')
			for team in teams:
				dictionary[int(team)].append(str(index + 1))

		entries = []
		for key, values in sorted(dictionary.items(), key=lambda x: x[0]):
			entries.append("{}:{}".format(key, ','.join(values)))

		print('; '.join(entries) + ';')