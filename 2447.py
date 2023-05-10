import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr = []


def recur(s_y, s_x, size, check):
    if size == 1:
        if check:
            arr[s_y][s_x] = '*'
        else:
            arr[s_y][s_x] = ' '
        return

    nxt = int(size//3)

    if check:
        recur(s_y, s_x, nxt, True)
        recur(s_y, s_x + nxt, nxt, True)
        recur(s_y, s_x + 2*nxt, nxt, True)

        recur(s_y+nxt, s_x, nxt, True)
        recur(s_y+nxt, s_x + nxt, nxt, False)
        recur(s_y+nxt, s_x + 2*nxt, nxt, True)

        recur(s_y+2*nxt, s_x, nxt, True)
        recur(s_y+2*nxt, s_x + nxt, nxt, True)
        recur(s_y+2*nxt, s_x + 2*nxt, nxt, True)

    else:
        for i in range(s_y, s_y+size):
            for j in range(s_x, s_x+size):
                arr[i][j] = ' '


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    arr = [[0 for __ in range(n)] for __ in range(n)]

    recur(0, 0, n, True)

    for i in arr:
        for j in i:
            print(j, end="")
        print()
