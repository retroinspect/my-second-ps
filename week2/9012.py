def isValidPs(ps):
    opened = 0
    for p in ps:
        if p == '(':
            opened += 1
        else:
            opened -= 1
        
        if opened < 0:
            return False
    
    return opened == 0

num = int(input())
for i in range(num):
    ps = input()
    answer = isValidPs(ps)
    if (answer):
        print("YES")
    else:
        print("NO")
