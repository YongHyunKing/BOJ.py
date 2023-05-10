import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = [[0 for __ in range(n+1)] for __ in range(n+1)]
    dp = [[0 for __ in range(n+1)] for __ in range(n+1)]
    for i in range(1, n+1):
        li = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(1, n+1):
            arr[i][j] = li[j-1]

    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] + arr[i][j] - dp[i-1][j-1]

    for i in range(m):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
        print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
