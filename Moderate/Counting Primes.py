import sys

def is_prime(num):
	for div in range(2, int(num ** 0.5) + 1):
		if num % div == 0:
			return False

	return True

def primes_between(N, M):
	result = 0

	for num in range(N, M+1):
		if is_prime(num):
			result += 1

	return result

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		N, M = list(map(int, test.strip().split(',')))
		print(primes_between(N, M))