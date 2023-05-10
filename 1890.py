import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline().rstrip())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    dp = [[0 for __ in range(n)] for __ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                jump = arr[i][j]
                if i+jump < n:
                    dp[i+jump][j] += dp[i][j]
                if j+jump < n:
                    dp[i][j+jump] += dp[i][j]

    print(dp[n-1][n-1])
