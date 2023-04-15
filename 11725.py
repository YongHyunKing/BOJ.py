import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque

check = [-1 for __ in range(100001)]
arr = [[] for __ in range(100001)]

def bfs(start):
    check[start] = 0
    que = Queue()
    que.put(start)
    
    while not que.empty():
        cur = que.get()
        for nxt in arr[cur]:
            if check[nxt] == -1:
                check[nxt] = cur
                que.put(nxt)
    

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())

    for i in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)
        
    bfs(1)

    for i in check:
        if i!=0 and i!=-1:
            print(i)