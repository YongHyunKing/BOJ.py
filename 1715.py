from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key
import heapq

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    l = list(map(int,s.readlines()))
    pq = []
    for i in l:
        heapq.heappush(pq,i)
    
    ans = 0
    while len(pq)!=1:
        a,b=heapq.heappop(pq),heapq.heappop(pq)
        ans+=(a+b)
        heapq.heappush(pq,a+b)
        
    print(ans)
    
