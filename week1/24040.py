def is_pretty_cake(N):
    if N % 3 == 2:
        return True

    if N % 9 == 0:
        return True
    
    return False


import sys
input = sys.stdin.readline

T = int(input())
inputs = []
for t in range(T):
    N = int(input())
    inputs.append(N)


for N in inputs:
    if (is_pretty_cake(N)):
        print("TAK")
    else:
        print("NIE")

