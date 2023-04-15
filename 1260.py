import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from functools import cmp_to_key

arr = None
check = []

def bfs(start):
    que=Queue()
    que.put(start)
    check[start] = True  
    while not que.empty():
        cur = que.get()
        print(cur, end=" ")
        for nxt in arr[cur]:
            if not check[nxt]:
                check[nxt] = True
                que.put(nxt)
            
            
def dfs(cur):
    check[cur] = True
    print(cur, end = " ")
    for nxt in arr[cur]:
        if not check[nxt]:
            check[nxt] = True
            dfs(nxt)
    


if __name__ == "__main__":
    #sys.stdin = open('input.txt', 'rt')
    n,m,v = map(int,sys.stdin.readline().split())
    arr = [[]for __ in range(1001)]
    
    for i in range(m):
        s,e = map(int,sys.stdin.readline().split())
        arr[s].append(e)
        arr[e].append(s)
    
    for i in range(1001): arr[i] = sorted(arr[i])
    check = [False for _ in range(1001)]
    dfs(v)
    print()
    check = [False for _ in range(1001)]
    bfs(v)


    

