import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr,dist=[],[] 
n,m,k = None,None,None
flag = False
def dijkstra(start,end):
    pq = []
    dist[start] = 0
    heappush(pq,[0,start])
    while pq:
        p = heappop(pq)
        if p[1] == end:
            print(p[0])
            return
        for nxt in arr[p[1]]:
            if nxt[0]+dist[p[1]]<dist[nxt[1]]:
                dist[nxt[1]] = nxt[0]+dist[p[1]]
                heappush(pq,[dist[nxt[1]],nxt[1]])
    

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    arr = [[] for __ in range(n+1)]
    dist = [sys.maxsize for __ in range(n+1)]
    
    for i in range(m): 
        a,b,w = map(int,sys.stdin.readline().split())
        arr[a].append([w,b])
        
    start,end = map(int,sys.stdin.readline().split())
    dijkstra(start,end)
