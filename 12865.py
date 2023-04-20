import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,k = map(int,sys.stdin.readline().rstrip().split())
    dp = [[0 for __ in range(k+1)] for __ in range(n+1)]
    arr = []
    
    for i in range(n) : arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    for i in range(1,n+1):
        w,v = arr[i-1]
        for j in range(1,k+1):
            if j-w>=0 : dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
            else : dp[i][j] = dp[i-1][j]

    print(dp[n][k])
