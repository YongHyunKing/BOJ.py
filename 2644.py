import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop



if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    check = [False] * (n+1)
    arr = [[] for __ in range(n+1)]
    s,e = map(int,sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    
    for i in range(m):
        a,b = map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)
    
    q = deque()
    
    q.append([s,0])
    check[s] = True
    ans = -1
    while q:
        cur, c = q.popleft()
        if cur == e:
            ans = c
            break
        
        for nxt in arr[cur]:
            if not check[nxt]:
                check[nxt] = True
                q.append([nxt,c+1])
                
    print(ans)

