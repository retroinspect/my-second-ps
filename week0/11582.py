def merge(list1, list2):
    result = []
    length = len(list1)
    p1 = 0
    p2 = 0
    
    while p1 < length and p2 < length:
        if list1[p1] <= list2[p2]:
            q1 = p1
            while q1 < length and list1[q1] <= list2[p2]:
                q1 += 1
            
            result += list1[p1:q1] + [list2[p2]]
            p1 = q1
            p2 += 1

        else:
            q2 = p2
            while q2 < length and list2[q2] < list1[p1]:
                q2 += 1
            
            result += list2[p2:q2] + [list1[p1]]
            p2 = q2
            p1 += 1

    
    if p1 == length and p2 == length:
        return result

    if p1 < length:
        return result + list1[p1:]
    
    if p2 < length:
        return result + list2[p2:]

def merge(list1, list2):
    result = list1 + list2
    result.sort()
    return result

# TOP DOWN ()
# BOTTOM UP 

# [1, 2, 3, 4] => [1, 2] [3, 4]
def getKStepSort(N, nums, k):
    size = 1
    while size < N / k:
        # print(nums)
        nums = [merge(nums[2*i], nums[2*i+1]) for i in range(len(nums)//2)]
        size *= 2
    
    return [num for l in nums for num in l]

import sys
input = sys.stdin.readline

N = int(input())
nums = [[int(c)] for c in input().split(' ')]
k = int(input())

answer = getKStepSort(N, nums, k)
print(' '.join(map(str, answer)))