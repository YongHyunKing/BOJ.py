import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    arr,tmp,pq = [],[],[]
    for i in range(n): tmp.append(list(map(int,sys.stdin.readline().split())))
    d = int(sys.stdin.readline())

    for i in tmp:
        a,b = i
        if a>b: a,b=b,a
        if b-a>d: continue
        arr.append([a,b])
        
    arr.sort(key = lambda x : x[1])
    # print(arr)
    maax = 0
    for i in arr:
        s,e = i
        road_end = e-d
        heappush(pq,s)
        while pq and pq[0]<road_end: heappop(pq)
        maax = max(maax,len(pq))
    print(maax)
        
