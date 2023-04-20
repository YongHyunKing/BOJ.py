import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

go=[]
back=[]
dist = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    go = [[] for __ in range(n+1)]
    back = [[] for __ in range(n+1)]
    check = [False for __ in range(n+1)]
    dist = [-sys.maxsize for __ in range(n+1)]
    in_cnt = [ 0 for __ in range(n+1)]
    in_cnt2 = [ 0 for __ in range(n+1)]
    
    for i in range(m):
        a,b,c = map(int,sys.stdin.readline().rstrip().split())
        go[a].append([b,c])
        in_cnt[b]+=1
        
    start, end = map(int, sys.stdin.readline().split())
        
    q = deque()
    
    q.append([start,0])
    dist[start] = 0  
    while q:
        cur,c = q.popleft()
        for nxt,nxt_c in go[cur]:
            if dist[nxt] <  c + nxt_c :
                dist[nxt] = c + nxt_c
                back[nxt] = [cur]
                in_cnt2[nxt] = 1
            elif dist[nxt] == c + nxt_c:
                back[nxt].append(cur)
                in_cnt2[nxt] +=1
            in_cnt[nxt]-=1
            if in_cnt[nxt] == 0 : q.append([nxt,dist[nxt]])
            
    print(dist[end])
    ans = 0
    q.append(end)

    while q:
        cur = q.popleft()
        for nxt in back[cur]:
            ans+=1
            if not check[nxt] : 
                check[nxt] = True
                q.append(nxt)
    
    print(ans)