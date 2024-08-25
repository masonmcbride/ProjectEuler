# Project euler problem 3
# projecteuler.net/problem=3

import math


# What is the largest prime factor of the number 600851475143
def compute():
    N = 600851475143
    i = 2
    while N > i:
        if N % i == 0:
            N /= i
        else:
            i += 1
    return str(i)

if __name__ == '__main__':
    print(compute())
