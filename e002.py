# Solution to Project euler problem 2
# https://projecteuler.net/problem=2
# copy with y(ank) + shift + w 

# sum of even fib numbers < 4 million
def compute():
    total = 0
    a = 0
    b = 2

    while a <= 4000000:
        total += a
        a, b = b, (4*b + a)
        
    return str(total)

if __name__ == '__main__': 
    print(compute())


# E(n) = 4*E(n-1) + E(n-2)
# E(n+1) = 4*E(n) + E(n-1)
# because it's equivalent
# F(n) = 4*F(n-3) + F(n-6)
# F(n) = 
