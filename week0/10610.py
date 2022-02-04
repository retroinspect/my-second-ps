# N의 각 자리 수의 합은 3의 배수여야 함
# N의 자리수 중에는 적어도 1개의 0이 있어야 함

# 3의 배수 & 10의 배수
# 

def getMultipleOf30(N):
    digits = [ int(x) for x in str(N)]

    if 0 not in digits:
        return -1
    
    if sum(digits) % 3 != 0:
        return -1

    digits.sort(reverse=True)
    return int(''.join(map(str, digits)))

N = input()
answer = getMultipleOf30(N)
print(answer)