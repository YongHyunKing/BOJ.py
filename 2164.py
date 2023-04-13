from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    que = deque()
    for i in range(1,n+1):
        que.append(i)
        
    while len(que)!=1:
        que.popleft()
        que.append(que.popleft())
        
    print(que[0])

