# Project euler problem #016
# projecteuler.net/problem=16
# projecteuler.net/thread=16
# author: mason


def compute():
    num = str(2**1000)
    ans = 0
    for digit in num:
        ans += int(digit)
    return ans

if __name__ == '__main__':
    print(compute())