# Project euler problem #015
# projecteuler.net/problem=15
# projecteuler.net/thread=15
# author: mason

from functools import cache

def compute():
    return num_paths(20,20)

@cache
def num_paths(m,n) -> int:
    if m == 0 or n == 0: 
        return 1
    return num_paths(m-1,n) + num_paths(m,n-1)

if __name__ == '__main__':
    print(compute())