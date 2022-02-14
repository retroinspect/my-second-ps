
from collections import deque as Queue

answer = []
N, K = map(int, input().split(' '))

q = Queue(list(range(1, N+1)))

count = 0
while len(q) > 0:
    size = len(q)
    count += 1
    popped = q.popleft()
    # print(count, popped, (K % size), size)
    if (K % size) == count or ((K % size) == 0 and count == size):
        answer.append(str(popped))
        count = 0
    else:
        q.append(popped)

print('<%s>' % ', '.join(answer))