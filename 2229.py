import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if n == 1:
        print(0)
    else:
        cost = 0
        tmp = abs(arr[1]-arr[0])
        miin = min(arr[1], arr[0])
        for i in range(2, n-1):
            # 왼쪽 나누어지는 경우, 오른쪽 포함되는 경우
            if tmp + abs(arr[i]-arr[i+1]) > max(tmp, abs(miin - arr[i])):
                cost += tmp
                tmp = abs(arr[i]-arr[i+1])
                miin = min(arr[i], arr[i+1])
                i += 1
            else:
                tmp = max(tmp, abs(miin - arr[i]))
                miin = min(miin, arr[i])

    print(tmp)
    print(cost)
