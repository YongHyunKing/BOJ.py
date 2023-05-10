import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

m, n = None, None
arr = []
dp = []
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]

cnt = 1


def dfs(y, x):

    if y == n-1 and x == m-1:
        return 1
    dp[y][x] = 0

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < m and arr[y][x] > arr[ny][nx]:
            if dp[ny][nx] == -1:
                dp[y][x] += dfs(ny, nx)
            else:
                dp[y][x] += dp[ny][nx]

    return dp[y][x]


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n, m = map(int, sys.stdin.readline().rstrip().split())

    dp = [[-1 for __ in range(m)] for __ in range(n)]

    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    print(dfs(0, 0))
