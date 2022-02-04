from bisect import bisect

def getFriends(s, k):
    friends = 0
    p = len(s) - 1
    i = 0
    while i < p:
        end = min(i+k, p)

        # search max j such that s[i] <= s[j] <= s[i] + k where i <= j <= end
        l = bisect(s, s[i] + k, i, end)
        x = l-i+1
        friends += x*(x-1)//2
        print(x)
        i = l

    return friends

import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))
hash_table = dict()
for i in range(N):
    name = input().strip()
    if len(name) in hash_table.keys():
        hash_table[len(name)].append(i)
    else:
        hash_table[len(name)] = [i]

print(hash_table)

answer = 0

for list in hash_table.values():
    print(list)
    answer += getFriends(list, K)

print(answer)