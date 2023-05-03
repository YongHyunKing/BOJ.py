import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

dy, dx = [0,0,-1,1],[1,-1,0,0]
check,arr,tmp = [],[],[]
n,k,s,ex,ey = None,None,None,None,None


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,k = map(int,sys.stdin.readline().rstrip().split())
    
    check = [[0 for __ in  range(n)] for __ in range(n)]
    
    for i in range(n) : arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    s,ex,ey = map(int,sys.stdin.readline().rstrip().split())
    
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] :
                tmp.append([arr[i][j],i,j])
                check[i][j] = arr[i][j]
    
    tmp.sort()
    q = deque()
    
    for num,y,x in tmp : q.append([y,x,num])
    
    while q:
        if s!=0:
            size = len(q)
            s-=1
            for p in range(size):
                y,x,num = q.popleft()
                for i in range(4):
                    ny,nx = y+dy[i], x+dx[i]
                    if 0 > ny or ny >= n or 0 > nx or nx >= n : continue
                    if check[ny][nx] : continue
                    check[ny][nx] = num
                    q.append([ny,nx,num])
        else : break

    print(check[ex-1][ey-1])
