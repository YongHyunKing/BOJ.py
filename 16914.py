import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop
from functools import cmp_to_key
sys.setrecursionlimit(10**5)
sa, group, tmp = [], [], []
d = 1
n = None


def cmp(a, b):
    if group[a] == group[b]:
        if group[min(a+d, n)] == group[min(b+d, n)]:
            return 0
        return 1
    return 1


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')

    string = sys.stdin.readline().rstrip()
    n = len(string)

    for i in range(n):
        sa.append(i)
        group.append(ord(string[i]))

    group.append(-1)
    string += '$'

    tmp = [0]*(n)

    while d <= n:
        sa.sort(key=lambda x: (group[x], group[min(x+d, n)]))

        for i in range(n-1):
            tmp[i+1] = tmp[i] + cmp(sa[i+1], sa[i])
        for i in range(n):
            group[sa[i]] = tmp[i]
        if tmp[n-1] == n:
            break
        d <<= 1

    lcp = [0] * (n)
    prefix = [0] * n
    k = 0
    ans = []
    for i in range(n):
        k = max(k-1, 0)
        if group[i] == 0:
            continue

        j = sa[group[i]-1]
        while string[i+k] == string[j+k]:
            k += 1
        lcp[group[i]] = k

    prefix[0] = n - sa[0] - lcp[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + n - sa[i] - lcp[i]
    result = 0

    t = int(sys.stdin.readline())

    for z in range(t):
        q = int(sys.stdin.readline())

        if q > prefix[-1]:
            print(-1)
            continue
        left, right = 0, n-1
        idx = 0
        while (left <= right):
            mid = int((left+right)//2)
            if prefix[mid] >= q:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        # print("idx", idx)
        seq = q
        if idx != 0:
            seq -= prefix[idx-1]

        print(string[sa[idx]:sa[idx]+lcp[idx]+seq])
