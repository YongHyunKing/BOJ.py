import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop
arr = []
dp = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    for i in range(n) : arr.append(list(map(int,sys.stdin.readline().split())))
    dp = [[0 for __ in range(n)] for __ in range(n)]
    
    for j in range(n):
        for i in range(n-j):
            y,x = i,i+j
            if y==x: dp[y][x] = 0
            else:
                dp[y][x] = sys.maxsize
                for k in range(y,x):
                    dp[y][x] = min(dp[y][x],dp[y][k]+dp[k+1][x]+arr[y][0]*arr[k][1]*arr[x][1])
                    
    print(dp[0][n-1])