import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

sys.setrecursionlimit(10**5)

dp = []
n = None
INF = 10**9

def dfs(cur,speed):
    if cur>n : return INF
    if not rock[cur] : return INF
    if dp[cur][speed] : return dp[cur][speed]
    if cur == n : return 1
    
    dp[cur][speed] = INF
    for i in range(-1,2):
        nxt = speed+i
        if nxt > 0 : dp[cur][speed] = min(dp[cur][speed],dfs(cur+nxt,nxt)+1)
    
    return dp[cur][speed]

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,m = map(int,sys.stdin.readline().split())
    dp = [[0 for __ in range(int((2*n)**0.5+1))] for __ in range(n+1)]
    rock = [True for __ in range(n+1)]
    
    for i in range(m):
        rock[int(sys.stdin.readline())] = False
    
    ans = dfs(2,1)
    if ans == INF : print(-1)
    else : print(ans)

