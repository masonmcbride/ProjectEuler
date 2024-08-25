# Project euler problem 5
# projecteuler.net/problem=5

from math import lcm 

def compute():
    return lcm(*range(1,21))

if __name__ == '__main__':
    print(compute())