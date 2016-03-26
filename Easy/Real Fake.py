import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		total = 2 * int(test[0]) + int(test[1]) + 2 * int(test[2]) + int(test[3]) + 2 * int(test[5]) + int(test[6]) + 2 * int(test[7]) + int(test[8]) + 2 * int(test[10]) + int(test[11]) + 2 * int(test[12]) + int(test[13]) + 2 * int(test[15]) + int(test[16]) + 2 * int(test[17]) + int(test[18])

		if total % 10 == 0:
			print("Real")
		else:
			print("Fake")