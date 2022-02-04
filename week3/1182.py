# 부분수열: 연속되지 않아도 됨. 그러나 순서는 원래 순열의 순서와 같아야 함

N, S = map(int, input().split(' '))
nums = list(map(int, input().split( )))

cnt = 0

def getSum(current, idx, cnt):
    if current + nums[idx] == S:
        cnt += 1

