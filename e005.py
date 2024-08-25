# Project euler problem 5
# projecteuler.net/problem=5


def compute():
    pass

if __name__ == '__main__':
    print(compute())

# 1|n, 2|n, 3|n, ..., 20|n = min(n : Z) 

# recall: a|b iff k * a = b
"""
so 1|n = k1 * 1 = N => n is trivially k1 in this case
   2|n = k2 * 2 = N
   3|n = k3 * 3 = N
   4|n = k4 * 4 = N
   5|n = k5 * 5 = N
   ...
   20|n = k20 * 20 = N

"""
