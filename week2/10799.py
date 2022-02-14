input = input().replace("()", "L")

throughing = 0
total_stick = 0
for cmd in input:
    if cmd == '(':
        total_stick += 1
        throughing += 1
    elif cmd == ')':
        throughing -= 1
    else:
        total_stick += throughing

print(total_stick)