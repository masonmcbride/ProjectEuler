# Project euler problem #310
# projecteuler.net/problem=310
# projecteuler.net/thread=310 
# author: mason m.

import math

# PROBLEM- 
# nim subtraction game where player can only removes square amount of chips from pile
# there are three piles and I need to find how many winnings moves exist 
def compute():

    # first pass: compute nimbers of a single heap of sub-a-sq nim
    # second pass: build up a list by xoring up 3 nim values for piles a b c

    # to compute from a graph is the sum of left and the sum of right
    return A014586_list(10)

def sub_a_sq_nimbers(n):
    nimbers = []
    for i in range(n+1):
        moves = [i - a**2 for a in range(1, math.isqrt(n))]
        moves.sort()
        mex = next((j for j in range(len(moves)) if moves[j] != j), len(moves))
        nimbers.append(mex)

    return nimbers


if __name__ == '__main__':
    print(compute())
