import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop
import copy

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    arr = []
    for i in range(n):
        if a[i] != b[i]:
            arr.append(0)
        else:
            arr.append(1)

    cnt1, cnt2 = 0, 0
    arr2 = copy.deepcopy(arr)
    for i in range(1, n):
        if not arr[i-1]:
            cnt1 += 1
            arr[i-1] += 1
            arr[i] = int((arr[i]+1) % 2)
            if i != n-1:
                arr[i+1] = int((arr[i+1]+1) % 2)
    # print(arr)
    if not arr[n-1]:
        cnt1 = sys.maxsize

    arr2[0] = int((arr2[0]+1) % 2)
    arr2[1] = int((arr2[1]+1) % 2)
    cnt2 += 1
    for i in range(1, n):
        if not arr2[i-1]:
            cnt2 += 1
            arr2[i-1] += 1
            arr2[i] = int((arr2[i]+1) % 2)
            if i != n-1:
                arr2[i+1] = int((arr2[i+1]+1) % 2)

    # print(arr2)
    if not arr2[n-1]:
        cnt2 = sys.maxsize

    ans = min(cnt2, cnt1)

    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)
