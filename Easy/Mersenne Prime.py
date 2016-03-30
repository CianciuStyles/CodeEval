import math
import sys

def is_prime(num):
	for div in range(2, int(math.sqrt(num)) + 1):
		if num % div == 0:
			return False

	return True

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == "":
			continue

		limit = int(test)
		num, p, mersenne_primes = 3, 2, []
		while num < limit:
			num = 2 ** p - 1
			if is_prime(num) is True:
				mersenne_primes.append(str(num))

			p += 1

		print(", ".join(mersenne_primes))