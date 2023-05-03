import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

n,m = None, None
ans = 0
arr = []
dy = [-1,1,0,0,1,1,-1,-1]
dx = [0,0,1,-1,1,-1,1,-1]

def bfs(a,b):
    check = [[False for __ in range(m)] for __ in range(n)]
    q = deque()
    q.append([a,b])
    check[a][b] = True
    cnt = 0
    while q:
        size = len(q)
        cnt+=1
        for k in range(size):
            y,x = q.popleft()
            # if a == n -1 and b == m - 1 : print(y,x)
            for l in range(8):
                ny,nx = y+dy[l], x+dx[l]
                if 0<=ny<n and 0<=nx<m:
                    if not arr[ny][nx] and not check[ny][nx]:
                        check[ny][nx] = True
                        q.append([ny,nx])
                    elif arr[ny][nx]:
                        return cnt
                    
                    
    return cnt

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,m = map(int, sys.stdin.readline().rstrip().split())
    
    
    for i in range(n) : arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    for i in range(n):
        for j in range(m):
            
            if not arr[i][j] : 
                ans = max(ans,bfs(i,j))
                # print(i,j,ans)
    
    
    print(ans)
