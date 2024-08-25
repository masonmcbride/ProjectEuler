# Project euler #007
# projecteuler.net/problem=7
# projecteuler.net/thread=7
# author: mason m.

def compute()
    N = 10001
    primes = by_prime_sieve(10001)
    return primes[10000]

if __name__ == '__main__':
    print(compute())
