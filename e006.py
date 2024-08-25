# Project euler problem #006
# projecteuler.net/problem=6
# projecteuler.net/thread=6
# author: mason

def compute():
    N = 100
    ans = square_of_sum(N) - sum_of_squares(N) 
    return(str(ans))

def square_of_sum(n):
    sum_of_nats = (n * (n+1)) / 2
    return sum_of_nats ** 2

def sum_of_squares(n):
    return (n * (n+1) * (2*n + 1)) / 6

if __name__ == '__main__':
    print(compute())
