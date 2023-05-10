import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop


def recur(st, size, check):
    if size == 0:
        return

    if not check:
        for i in range(st, st+size):
            arr[i] = ' '
    else:
        nxt = int(size//3)
        recur(st, nxt, True)
        recur(st+nxt, nxt, False)
        recur(st+2*nxt, nxt, True)


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    ns = list(map(int, sys.stdin.readlines()))

    for n in ns:
        arr = ['-' for __ in range(3**n)]
        recur(0, 3**n, True)
        for i in arr:
            print(i, end="")
        print()
