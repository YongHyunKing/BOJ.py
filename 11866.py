from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,k = map(int,s.readline().split())
    deq = deque()
    for i in range(1,n+1): deq.append(i)
    ans = []
    cnt = k-1
    while len(deq)!=0:
        if cnt == 0:
            cnt = k-1
            ans.append(deq.popleft())
        else:
            deq.append(deq.popleft())
            cnt-=1
            
    print("<",end="")
    for i in range(len(ans)):
        print(ans[i],end="")
        if i == len(ans)-1:print(">")
        else : print("",end=", ")

