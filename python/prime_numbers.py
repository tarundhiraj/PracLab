def get_primes(n):
	sieve = [True] * n
	sieve[0] = sieve[1] = False

	for i in range(2,n):
		if not sieve[i]: continue
		sieve[i*2::i] = [False] * len(sieve[i*2::i])


	primes = []

	for i,v in enumerate(sieve):
		if v: primes.append(i)

	return primes

print(get_primes(1000))