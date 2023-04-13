from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    que = deque()
    n = int(s.readline())
    
    for i in range(n):
        cmd = list(s.readline().split())
        # print(que,cmd[0])
        if cmd[0] == "push": que.append(cmd[1])
        elif cmd[0] == "pop" :
            if len(que)==0: print(-1)
            else : print(que.popleft())
        elif cmd[0] == "size": print(len(que))
        elif cmd[0] == "empty":
            if len(que) == 0: print(1)
            else : print(0)
        elif cmd[0] == "front":
            if len(que)==0: print(-1)
            else : print(que[0])
        elif cmd[0] == "back":
            if len(que)==0: print(-1)
            else : print(que[len(que)-1])