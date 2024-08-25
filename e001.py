# Solution to Project euler problem 1
# https://projecteuler.net/problem=1
# copy with y(ank) + shift + w 

def compute():
    ans = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
    return (str(ans))

if __name__ == '__main__': 
    print(compute())
