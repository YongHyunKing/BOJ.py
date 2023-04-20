import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr = []
cost = []
in_cnt = []
check = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline().rstrip())
    arr=[[] for __ in range(n+1)]
    cost=[0 for __ in range(n+1)]
    check=[False for __ in range(n+1)]
    in_cnt = [0 for __ in range(n+1)]
    m = int(sys.stdin.readline().rstrip())
    
    
    for i in range(m):
        a,b,w = map(int,sys.stdin.readline().rstrip().split())
        arr[a].append([b,w])
        in_cnt[b]+=1
    
    q = deque()
    for i in range(1,n+1):
        if in_cnt[i] == 0 :
            q.append(i)
            cost[i]=1
        
    
    while q:
        num = q.popleft()
        for nxt,c in arr[num]:
            check[num]=True
            in_cnt[nxt]-=1
            if in_cnt[nxt] == 0: q.append(nxt)
            cost[nxt]+=c*cost[num]
    
    for i in range(1,n+1):
        if not check[i] : print(i,cost[i])
            
        

