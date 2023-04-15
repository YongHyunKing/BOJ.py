import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr,dist=[],[]
dy,dx = [-1,1,0,0],[0,0,-1,1]
n,m,k = None,None,None
flag = False
def dijkstra():
    pq = []
    dist[0][0] = 0
    heappush(pq,[0,0,0])
    while pq:
        w,y,x = heappop(pq)
        if w > dist[y][x] : continue
        for i in range(4):
            ny, nx = y+dy[i],x+dx[i]
            nxt_w = 0
            if 0<=ny<n and 0<=nx<n :
                if arr[ny][nx] == '0': nxt_w+=1
                if nxt_w+w < dist[ny][nx]:
                    dist[ny][nx]=nxt_w+w
                    heappush(pq,[dist[ny][nx],ny,nx])
            
    

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    for i in range(n): arr.append(sys.stdin.readline().rstrip())
    dist = [[sys.maxsize for __ in range(n)]for __ in range(n)]
        
    dijkstra()
    print(dist[n-1][n-1])

