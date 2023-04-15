import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop


arr,dist,check=[],[],[]
dy,dx = [-1,1,0,0],[0,0,-1,1]
deq = deque()

def bfs(s_y,s_x):
    check2 = [[False for __ in range(m)]for __ in range(n)]
    que = Queue()
    que.put([s_y,s_x])
    check[s_y][s_x] = True
    while not que.empty():
        y,x = que.get()
        
        for i in range(4):
            if 0<=ny<n and 0<=nx<m and arr[ny][nx]==0:
                check[y][x]=True
                deq.append([y,x])
                break
        
        for i in range(4):
            ny, nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m :
                if not check2[ny][nx] and arr[ny][nx]!=0:
                    check2[ny][nx] = True
                    que.put([ny,nx])
                    


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n, m = map(int,sys.stdin.readline().split())
    for i in range(n): arr.append(list(map(int,sys.stdin.readline().split())))
    check = [[False for __ in range(m)]for __ in range(n)]
    cnt = 0
    
    for i in range(1,n-1):
        for j in range(1,m-1):
            if not check[i][j] and arr[i][j]>0: bfs(i,j)
                
    while 1:
        flag = False
        for i in range(1,n-1):
            for j in range(1,m-1):
                if arr[i][j]>0: 
                    flag=True
        
        if not flag :
            print(0)
            break
        

        size = len(deq)
        
        for j in range(size):
            y,x = deq.popleft()
            cnt1 = 0
            for i in range(4):
                ny, nx = y+dy[i],x+dx[i]
                if 0<=ny<n and 0<=nx<m and arr[ny][nx]==0: cnt1+=1
            
            if arr[y][x]-cnt1<=0:
                arr[y][x] = 0
                for i in range(4):
                    ny, nx = y+dy[i],x+dx[i]
                    if 0<=ny<n and 0<=nx<m and not check[ny][nx] and arr[ny][nx]!=0:
                        check[ny][nx]=True
                        deq.append([ny,nx])
            else :
                arr[y][x]-=cnt1 
                deq.append([y,x])
        
        dfs(0,0)
                
        
                    
        cnt+=1
                    