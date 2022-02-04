import sys
input = sys.stdin.readline

class Stack:
    elements = []
    def __init__(self):
        self.elements = []

    def push(self, e):
        self.elements.append(e)

    def pop(self):
        if self.empty():
            return -1
        return self.elements.pop(self.size()-1)

    def size(self):
        return len(self.elements)

    def empty(self):
        return len(self.elements) == 0

    def top(self):
        if self.empty():
            return -1
        return self.elements[self.size()-1]

n = int(input())
s = Stack()

for i in range(n):

    cmd = input().split(' ')
    cmd[0] = cmd[0].strip()

    if cmd[0] == "push":
        s.push(int(cmd[1]))
    elif cmd[0] == "top":
        print(s.top())
    elif cmd[0] == "pop":
        print(s.pop())
    elif cmd[0] == "size":
        print(s.size())
    elif cmd[0] == "empty":
        if s.empty():
            print(1)
        else:
            print(0)
