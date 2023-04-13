from sys import stdin as s
from typing import Sequence, MutableSequence

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    stack = []
    for i in range(n):
        num = int(s.readline())
        if len(stack) == 0:
            stack.append(num)
        else:
            while len(stack)!=0 and num>=stack[len(stack)-1]:
                 stack.pop()
            stack.append(num)
            
    print(len(stack))