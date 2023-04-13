from sys import stdin as s
from typing import Sequence, MutableSequence

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    stack = []
    
    for i in range(n):
        cmd = s.readline().split()
        if cmd[0] == "push": stack.append(cmd[1])
        elif cmd[0] == "pop":
            if len(stack)==0: print(-1)
            else: print(stack.pop())
        elif cmd[0]=="size": print(len(stack))
        elif cmd[0]=="empty":
            if len(stack)==0: print(1)
            else: print(0)
        else :
            if len(stack)==0: print(-1)
            else : print(stack[len(stack)-1])