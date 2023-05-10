import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')

    n = int(sys.stdin.readline().rstrip())
    arr = []
    ans = []
    cl = [0] * (n+1)
    for i in range(n):
        num, s, e = map(int, sys.stdin.readline().rstrip().split())
        ans.append(num)
        arr.append([s, e, num])
    arr.sort()

    pq = []
    dq = deque()
    cnt = 1
    dq.append(cnt)

    for i in range(n):
        s, e, num = arr[i]
        while len(pq) != 0 and pq[0][0] <= s:
            dq.append(heappop(pq)[1])

        if len(dq) == 0:
            cnt += 1
            dq.append(cnt)
        cl[num] = dq.popleft()

        heappush(pq, [e, cl[num]])

    print(cnt)
    for i in range(1, n+1):
        print(cl[i])
