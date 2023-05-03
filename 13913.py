import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

INF = 1000000

dist = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,k = map(int,sys.stdin.readline().split())
    dist = [[sys.maxsize,sys.maxsize]] * INF
    
    pq = []
    dist[n] = [0,n]
    heappush(pq,[0,n,n])
    ans = []
    
    while pq:
        cost, cur, fr = heappop(pq)
        
        if cost > dist[cur][0] : continue
        
        if cur == k:
            while dist[cur][1] != cur :
                ans.append(cur)
                cur = dist[cur][1]
            ans.append(cur)
            break
        
        if cur - 1>=0 and cost + 1 < dist[cur-1][0] :
            dist[cur-1] = [cost+1,cur]
            heappush(pq,[cost+1,cur-1,cur])
            
        if cur + 1<INF and cost + 1 < dist[cur+1][0] :
            dist[cur+1] = [cost+1,cur]
            heappush(pq,[cost+1,cur+1,cur])
            
        if cur * 2<INF and cost + 1 < dist[cur*2][0] :
            dist[cur*2] = [cost+1,cur]
            heappush(pq,[cost+1,cur*2,cur])
            
    print(len(ans)-1)
    for i in range(len(ans)-1,-1,-1) : print(ans[i], end = " ")
