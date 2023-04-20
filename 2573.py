import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(20000)

arr,dist,check=[],[],[]
dy,dx = [-1,1,0,0],[0,0,-1,1]
ice = deque()


def bfs(s_y,s_x,year):
    que = deque()
    que.append([s_y,s_x])
    
    while que:
        y,x = que.popleft()
        cnt=0
        for i in range(4):
            ny, nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m and check[ny][nx]!=year and arr[ny][nx]==0 :
                check[y][x] = year
                cnt+=1
        
        if cnt>=arr[y][x] : arr[y][x] = 0
        else : 
            arr[y][x] -= cnt
            ice.append([y,x])
        

        for i in range(4):
            ny, nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m and check[ny][nx]!=year and arr[ny][nx]!=0 :
                check[ny][nx] = year
                que.append([ny,nx])



if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n, m = map(int,sys.stdin.readline().split())
    for i in range(n): arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    check = [[-1 for __ in range(m)]for __ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] !=0 : ice.append([i,j])
    
    cnt = 0
    while 1:
        size = len(ice)
        if size == 0 :
            print(0)
            break
        
        flag = False
        for a in range(size):
            i, j = ice.popleft()
            if flag and check[i][j] != cnt:
                print(cnt)
                sys.exit()
            if flag and check[i][j] == cnt: continue    
            bfs(i,j,cnt)
            flag = True
        cnt+=1
            
            
