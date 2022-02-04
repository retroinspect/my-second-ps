def getSum(a, d, l, r):
    A_l = a + (l-1) * d
    A_r = a + (r-1) * d
    return (r-l+1) * (A_l+A_r) // 2


def gcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

    return b

def getGcd(a, d, l, r):
    A_l = a + (l-1) * d
    if l == r:
        return A_l
    return gcd(A_l+d, A_l)

# main
import sys
input = sys.stdin.readline

a, d = map(int, input().split(' '))
q = int(input())

queries = []
for i in range(q):
   cmd, l, r = map(int, input().split(' '))
   queries.append((cmd, l, r))

for query in queries:
    cmd, l, r = query
    if cmd == 1:
        print(getSum(a, d, l, r))
    else:
        print(getGcd(a, d, l, r))
