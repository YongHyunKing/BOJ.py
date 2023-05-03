import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

dy, dx = [0,0,-1,1],[1,-1,0,0]
check = []
arr =[]

def bfs(sy,sx):
    q = deque()
    q.append([sy,sx])
    cnt = 0
    while q:
        y,x = q.popleft()
        cnt+=1
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if 0 > ny or ny >= n or 0 > nx or nx >= n : continue
            if check[ny][nx] == True or arr[ny][nx] == '0' : continue
            check[ny][nx] = True
            q.append([ny,nx])
            
    return cnt

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    check = [[False for __ in  range(n)] for __ in range(n)]
    for i in range(n) : arr.append(sys.stdin.readline().rstrip())
    ans = []
    for i in range(n):
        for j in range(n):
            if not check[i][j] and arr[i][j] == '1':
                check[i][j]=True
                ans.append(bfs(i,j))
                
    ans.sort()
    print(len(ans))
    for i in ans : print(i)

