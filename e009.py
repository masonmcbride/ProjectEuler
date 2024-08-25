# Project euler problem #009
# projecteuler.net/problem=9
# projecteuler.net/thread=9
# author: mason

from math import gcd,prod

def compute():
    m = 2
    a,b,c = 0,0,0
    while a + b + c <= 1000:
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:  # Ensure coprime and m - n is odd
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if a + b + c == 1000: return (a,b,c)
                k = 2
                while k*a + k*b + k*c <= 1000:
                    if k*a + k*b + k*c == 1000: return (k*a, k*b, k*c)
                    k += 1
        m += 1

if __name__ == '__main__':
    print(prod(list(compute())))