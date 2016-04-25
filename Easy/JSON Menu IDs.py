import json
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test.strip() == '':
			continue

		json_doc = json.loads(test.strip())

		total = 0
		for item in json_doc["menu"]["items"]:
			try:
				if item["label"]:
					total += item["id"]
			except (KeyError, TypeError):
				continue

		print(total)