def brute_force(list, K):
    friends = 0
    for i in list: 
        for j in list:
            if i==j:
                continue 
            if i-j <= K and j-i <= K:
                friends += 1

    return friends // 2

from bisect import bisect, bisect_left

def getFriends(s, k):
    friends = 0
    p = len(s) - 1
    i = 0
    if p == 0:
        return 0

    while i <= p:
        # start = max(i-k, 0)
        # end = min(i+k, p)
        start = 0
        end = p

        # search min j such that s[i] - k <= s[j] <= s[i] where start <= j <= i
        l = bisect_left(s, s[i] - k, start, i)
        # search max j such that s[i] <= s[j] <= s[i] + k where i <= j <= end
        r = bisect(s, s[i] + k, i, end) - 1
        if s[i] + k >= s[end]:
            r += 1

        x = 0
        x += i-l
        x += r-i

        friends += x
        # print(r, l, x)
        i += 1

    return friends // 2

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

# print(hash_table)

answer = 0

for list in hash_table.values():
    # print(list)
    friends = getFriends(list, K)
    # bf_friends = brute_force(list, K)
    # if friends != bf_friends:
    #     print('brute force: ', bf_friends)
    #     print('getFriends: ', friends)
    answer += friends

print(answer)

