import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

go = []
check = []
ans = []
in_cnt = []

def dfs(cur):
    nxt = go[cur]
    ans.append(nxt)
    in_cnt[nxt] -=1
    if not check[nxt] : 
        check[nxt] = True
        dfs(nxt)

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    li = list(map(int,sys.stdin.readline().split()))
    check = [False] * (n+1)
    in_cnt = [0] * (n+1)
    go = [0 for __ in range(n+1)]
    
    for i in range(1,n+1) : 
        go[i] = li[i-1]
        in_cnt[li[i-1]]+=1
    
    li = []
    
    check[1]=True
    dfs(1)
    
    for i in range(1,n+1):
        if not check[i] and in_cnt[i] == 0: li.append(i)
    

    if li :
        for i in li : 
            if i != 1 : ans.append(i)
            check[i] = True
            dfs(i)
    
    
    for i in range(2,n+1):
        if not check[i] : 
            ans.append(i)
            check[i]=True
            dfs(i)
        
    print(len(ans))
    print(*ans)


