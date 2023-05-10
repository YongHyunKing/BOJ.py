import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = [sys.maxsize] * n
    cnt[0] = 0

    for i in range(n):
        for j in range(i, i+arr[i]+1):
            if j >= n:
                continue
            cnt[j] = min(cnt[j], cnt[i] + 1)

    if cnt[n-1] == sys.maxsize:
        print(-1)
    else:
        print(cnt[n-1])
