import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr,dist,check=[],[],[]
dy,dx,dz = [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]
s_x,s_y,e_x,e_y,n,m=[None] * 6
n,m,h = [None]*3
deq = deque()

def bfs(s_z,s_y,s_x,day):
    que = deq()
    que.put([s_z,s_y,s_x])
    check[s_z][s_y][s_x] = day
    cnt = 0
    while que:
        z,y,x = deq.popleft()
        cnt+=1
        for i in range(6):
            ny, nx,nz = y+dy[i],x+dx[i], z+dz[i]
            if 0<=z<h and 0<=ny<n and 0<=nx<m and arr[nz][ny][nx]==0 and not check[nz][ny][nx] :
                check[nz][ny][nx] = day
                arr[nz][ny][nx] = 1
                que.append([nz,ny,nx])
                
    return cnt

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    m,n,h = map(int,sys.stdin.readline().split())
    arr = [[] for __ in range(h)]
    
    for i in range(h):
        for j in range(n):
            arr[i].append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    check = [[[-1 for __ in range(m)] for __ in range(n)] for __ in range(h) ]
    toma = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == 0 : toma+=1
                elif arr[k][i][j] == 1 : deq.append([k,i,j])
                
    # print(arr)
    
    # for k in range(h):
    #     for i in arr[k]: print(i)
    if toma == 0:
        print(0)
        sys.exit()
    day = 0
    cnt = 0
    while 1 :
        day+=1
        size = len(deq)
        
        for l in range(size):
            z,y,x = deq.popleft()
            for i in range(6):
                ny, nx,nz = y+dy[i],x+dx[i], z+dz[i]
                if 0<=nz<h and 0<=ny<n and 0<=nx<m and arr[nz][ny][nx]==0 :
                    arr[nz][ny][nx] = 1
                    deq.append([nz,ny,nx])
                    toma-=1
    
        if toma == 0 :
            print(day)
            break
        if len(deq)==0:
            print(-1)
            break