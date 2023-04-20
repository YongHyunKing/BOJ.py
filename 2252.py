import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

in_cnt = []
arr = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,m = map(int, sys.stdin.readline().split())
    in_cnt = [0 for __ in range(n+1)]
    arr = [[] for __ in range(n+1)]
    
    q = deque()
    for i in range(m):
        a,b = map(int,sys.stdin.readline().split())
        arr[b].append(a)
        in_cnt[a]+=1
        
    for i in range(1,n+1):
        if in_cnt[i]==0:
            q.append(i)
    ans = []
    while q:
        num = q.popleft()
        ans.append(num)
        for i in arr[num]:
            in_cnt[i]-=1
            if in_cnt[i]==0: q.append(i)
            
    for i in range(len(ans)-1,-1,-1):
        print(ans[i], end = " ")
    
