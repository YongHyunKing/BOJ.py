import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr,dist,check=[],[],[]
dy,dx = [-1,1,0,0],[0,0,-1,1]
s_x,s_y,e_x,e_y,n,m=[None] * 6
deq = deque()

def bfs():
    que = Queue()
    que.put([s_y,s_x,0])
    check[s_y][s_x] = True
    while not que.empty():
        
        water = len(deq)
        
        for j in range(water):
            w_y,w_x = deq.popleft()
            for i in range(4):
                wy, wx = w_y+dy[i],w_x+dx[i]
                if 0<=wy<n and 0<=wx<m and arr[wy][wx] == '.':
                    arr[wy][wx] = '*'
                    deq.append([wy,wx])
        
        q = que.qsize()
        
        for k in range(q):
            y,x,w = que.get()
            
            for i in range(4):
                ny, nx = y+dy[i],x+dx[i]
                if 0<=ny<n and 0<=nx<m and not check[ny][nx] and (arr[ny][nx] == '.' or arr[ny][nx]=='D'):
                    if ny == e_y and nx==e_x:
                        print(w+1)
                        return True
                    check[ny][nx] = True
                    que.put([ny,nx,w+1])
                
    return False

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n, m = map(int,sys.stdin.readline().split())
    for i in range(n): arr.append(list(sys.stdin.readline().rstrip()))
    
    check = [[False for __ in range(m)] for __ in range(n) ]
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'D': e_y, e_x = i, j
            elif arr[i][j] == 'S': s_y, s_x = i,j
            elif arr[i][j] == '*': deq.append([i,j])

    if not bfs() : print('KAKTUS')
        