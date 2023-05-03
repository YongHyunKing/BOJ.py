import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop
from functools import cmp_to_key
sys.setrecursionlimit(10**5)


def cmp(a, b):
    if group[a] == group[b]:
        if group[min(a+d, n)] == group[min(b+d, n)]:
            return 0
        return 1
    return 1


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    t = int(sys.stdin.readline())
    for z in range(t):
        sa, group, tmp = [], [], []
        d = 1
        n = None
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

        cnt = 0
        lcp = [0] * (n)
        k = 0

        check = [0] * n
        for i in range(n):
            if check[i] == 1:
                cnt += 1

            k = max(k-1, 0)
            if group[i] == 0:
                continue
            j = sa[group[i]-1]

            while string[i+k] == string[j+k]:
                k += 1
            lcp[group[i]] = k

result = 0
for i in range(n-1):
    if lcp[i+1] > lcp[i]:
        result += lcp[i+1] - lcp[i]

        print(result)
