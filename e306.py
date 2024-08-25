# Project euler problem #306
# projecteuler.net/problem=306
# author: mason mcbride


def compute():
    return By_Spr_Gru_Thrm(50)


def By_Spr_Gru_Thrm(N):

    nimbers = {0: 0,
               1: 0}

    for n in range(2, N+1):
        nimbers[n] = mex([nimbers[k] ^ nimbers[n-2-k] for k in range(n-1)], N)

        if n % 1000 == 0:
            print(f"n = {n}")
    
    p2_wins = sum(1 for value in nimbers.values() if value == 0)
    return N - p2_wins + 1 # plus 1 for mappings[0] being 0 and not being a part of the game

def mex(table, N):
    for i in range(N):
        if i not in table:
            return i
    
if __name__ == '__main__':
    print(compute())
