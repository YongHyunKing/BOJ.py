import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

INF = 1000000000
dp = []
n = None
MAX = (1 << 10) - 1


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline().rstrip())
    dp = [[[0 for __ in range(MAX+1)] for __ in range(10)] for __ in range(n)]

    ans = 0
    for i in range(1, 10):
        dp[0][i][1 << i] = 1

    for i in range(0, n-1):
        for j in range(10):
            for k in range(1, MAX+1):
                if j > 0:
                    dp[i+1][j-1][1 << j-1 | k] += dp[i][j][k]
                    dp[i+1][j-1][1 << j-1 | k] %= INF
                if j < 9:
                    dp[i+1][j+1][1 << j+1 | k] += int(dp[i][j][k] % INF)
                    dp[i+1][j+1][1 << j+1 | k] %= INF

    for i in range(10):
        # print(dp[n-1][i][MAX])
        ans += dp[n-1][i][MAX]
        ans %= INF
    print(ans)
