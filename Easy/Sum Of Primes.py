import math

def is_prime(num):
	for div in range(2, int(math.sqrt(num)) + 1):
			if num % div == 0:
				return False

	return True

def generate_first_n_primes(n):
	primes = [2]
	num = 3
	while True:
		if is_prime(num):
			primes.append(num)
			if len(primes) == n:
				return primes
		num += 1

primes = generate_first_n_primes(1000)
print(sum(primes))