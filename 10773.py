from sys import stdin as s
from typing import Sequence, MutableSequence

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    stack = []
    
    for i in range(n):
        a = int(s.readline())
        if a == 0:
            stack.pop()
        else:
            stack.append(a)
            
    print(sum(stack))
