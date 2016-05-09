import collections
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		integer, decimal = test.strip().split('.')
		decimal = str(float('0.' + decimal) * 60)
		minutes, seconds = decimal.split('.')
		seconds = str(float('0.' + seconds) * 60).split('.')[0]

		print('{}.{}\'{}\"'.format(integer, minutes.zfill(2), seconds.zfill(2)))