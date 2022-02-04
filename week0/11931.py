import sys
input = sys.stdin.readline

N = input()
N = int(N)

nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)
for num in nums:
    print(num)