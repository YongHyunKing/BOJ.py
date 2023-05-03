import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,m = map(int,sys.stdin.readline().split())
    check = [[False for __ in range(m)] for __ in range(n)]
    arr = []
    for i in range(n) : arr.append(list(sys.stdin.readline().rstrip()))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not check[i][j]:
                cnt+=1
                if arr[i][j] == '-':
                    x = j
                    while x<m and arr[i][x]=='-':
                        check[i][x] = True
                        x+=1
                else:
                    y = i
                    while y<n and arr[y][j]=='|':
                        check[y][j] = True
                        y+=1
                        
    print(cnt)
