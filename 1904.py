import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

dp = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    dp = [0 for __ in range(1000001)]
    dp [0] = 0
    dp [1] = 1
    dp [2] = 2
    for i in range(3,n+1): dp[i] = (dp[i-1] + dp[i-2])%15746
    print(dp[n])

