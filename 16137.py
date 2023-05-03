import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr = []
n,m = None,None
dy, dx = [1,-1,0,0],[0,0,1,-1]


if __name__ == "__main__":
    #sys.stdin = open('input.txt', 'rt')
    n,m = map(int,sys.stdin.readline().rstrip().split())
    for i in range(n) : arr.append(list(map(int,sys.stdin.readline().split())))
    

    check = [[sys.maxsize for __ in range(n)] for __ in range(n)]
    check2 = [[sys.maxsize for __ in range(n)] for __ in range(n)]

    
    q = deque()
    q.append([0,0,0,False])
    check[0][0] = True
    
    while q:

        y,x,time,b = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if 0 > ny or ny >= n or 0 > nx or nx >= n : continue
            
            if not b :
                top,left,right,bottom = False, False, False, False
                    
                if arr[ny][nx]>=1 : 
                    add_time = arr[ny][nx] - time%arr[ny][nx]
                    if check[ny][nx] > add_time+time:
                        if arr[ny][nx]!=1 and arr[y][x]!=1 : continue
                        check[ny][nx] = add_time+time
                        q.append([ny,nx,add_time+time,b])
                        
                elif arr[ny][nx] == 0:
                    wall = [False] * 4
                    for j in range(4):
                        nny,nnx = ny+dy[j], nx+dx[j]
                        if 0<=nny<n and 0<=nnx<n and not arr[nny][nnx] : wall[i] = True
                    
                    if (wall[0] or wall[1]) and (wall[2] or wall[3]) : continue
                    add_time= m - time%m
                    if check[ny][nx] > add_time+time:
                        if arr[y][x]!=1 : continue
                        check[ny][nx] = add_time+time
                        q.append([ny,nx,add_time+time,True])

            elif b and arr[ny][nx] >= 1 : 
                    add_time= arr[ny][nx] - time%arr[ny][nx]
                    if check2[ny][nx] > add_time+time:
                        if arr[ny][nx]!=1 and arr[y][x]!=1 : continue
                        check2[ny][nx] = add_time+time
                        q.append([ny,nx,add_time+time,b]) 
            
    print(min(check[n-1][n-1],check2[n-1][n-1]))