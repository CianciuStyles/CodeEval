import sys

def generate_primes_up_to(upper_limit):
	return [x for x in range(2, upper_limit) if is_prime(x)]

def is_prime(num):
	for div in range(2, int(num ** 0.5) + 1):
		if num % div == 0:
			return False

	return True

with open(sys.argv[1], 'r') as test_cases:
	limits = []
	for test in test_cases:
		if test == '':
			continue

		N = int(test.strip())
		limits.append(N)
	
	primes = generate_primes_up_to(max(limits))
	for limit in limits:
		print(','.join([str(prime) for prime in primes if prime < limit]))