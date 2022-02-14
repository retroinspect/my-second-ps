
from collections import deque as Queue

answer = []
N = int(input())
nums = list(map(int, input().split(' ')))
q = Queue(list(range(1, N+1)))

K = 0
count = 0
right = True

while len(q) > 0:
    size = len(q)

    count += 1

    if right:
        popped = q.popleft()
    else:
        popped = q.pop()

    # print(count, popped, (K % size), size)
    if K == 0 or (K % size) == count or ((K % size) == 0 and count == size):
        answer.append(str(popped))
        count = 0
        right = nums[popped - 1] > 0
        K = abs(nums[popped - 1])

    else:
        if right:
            q.append(popped)
        else:
            q.appendleft(popped)

print(' '.join(answer))