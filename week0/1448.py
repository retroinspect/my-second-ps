def getMaxTriangleSum(nums):
    long = 0
    mid = 1
    short = 2
    
    while short < len(nums):
        if nums[long] >= nums[mid] + nums[short]:
            long += 1
            mid += 1
            short += 1
        else:
            return nums[long] + nums[mid] + nums[short]
    
    return -1

import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for __ in range(N)]
nums.sort(reverse=True)

answer = getMaxTriangleSum(nums)
print(answer)