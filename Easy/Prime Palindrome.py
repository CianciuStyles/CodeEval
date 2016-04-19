def generate_primes_up_to(upper_limit):
	primes = [2]
	i, p = 2, 0
	while True:
		if prime(i, primes):
			p += 1
			if p == upper_limit:
				return primes
		i += 1

def prime(i, primes):
	for prime in primes:
		if not (i == prime or i % prime):
			return False
	primes.append(i)
	return i

def is_palindrome(num):
	return str(num) == str(num)[::-1]

primes = generate_primes_up_to(1000)[::-1]
found = False

for prime in primes:
	if found is True:
		break

	if is_palindrome(prime) is True:
		print(prime)
		found = True