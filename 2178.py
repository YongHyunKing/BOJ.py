import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque

arr=[]
n,m = None, None
dy,dx = [-1,1,0,0], [0,0,-1,1]

def bfs():
    cnt = 0
    que = Queue()
    que.put([0,0,1])
    cnt+=1
    while not que.empty():
        p = que.get()
        for i in range(4):
            ny,nx = p[0]+dy[i], p[1]+dx[i]
            if 0<=ny<n and 0<=nx<m and arr[ny][nx]=='1' and check[ny][nx]==0:
                check[ny][nx] = p[2]+1
                if ny == n-1 and nx == m-1: return
                que.put([ny,nx,check[ny][nx]])


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,m = map(int,sys.stdin.readline().split())
    check = [[0 for __ in range(m)]for __ in range(n)]

    for i in range(n): arr.append(sys.stdin.readline().rstrip())
    bfs()
    print(check[n-1][m-1])
    
