import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        s,e = map(int,sys.stdin.readline().split())
        arr.append([e,s])
    arr.sort()
    
    ans = 0
    before = 0
    for i in arr:
        e,s = i
        if s >= before:
            ans+=1
            before = e
    
    print(ans)
        

