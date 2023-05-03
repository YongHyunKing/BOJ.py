import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline()
    cnt = [0] * 3
    ans = 0
    for i in s:
        if i == 'D':
            cnt[0] += 1
        elif i == 'K':
            cnt[1] += 1
        elif i == 'S':
            cnt[2] += 1
        elif i == 'H':
            ans += cnt[0]*cnt[1]*cnt[2]

    print(ans)
