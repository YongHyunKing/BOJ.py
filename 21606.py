import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
sys.setrecursionlimit(10**6)
# 0 : 외부, 1 : 산책로, 2 : 방문
check = []
visit = []
arr = []

def bfs(start):
    cnt = 0
    visit[start] = True
    que = Queue()
    que.put(start)
    
    while not que.empty():
        cur = que.get()
        for nxt in arr[cur]:
            if not visit[nxt] and check[nxt] == 0:
                visit[nxt] = True
                que.put(nxt)
            elif check[nxt] == 1:
                cnt+=1
    
    return cnt*(cnt-1)

def count(cur):
    # visit[cur] = True
    cnt = 0
    for nxt in arr[cur]:
        if check[nxt] == 1:
            cnt+=1

    return cnt
    
    

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()

    check.append(0)
    for i in s: check.append(int(i))
    visit = [False for __ in range(n+1)]
    arr = [[] for __ in range(n+1)]
    
    for i in range(n-1):
        a,b = map(int,sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)
        
    ans = 0
    for i in range(len(arr)):
        if not visit[i] and check[i] ==0:
            ans+=bfs(i)
    
    for i in range(len(arr)):
        if check[i] == 1:
            ans +=count(i)
            
    print(ans)
    
