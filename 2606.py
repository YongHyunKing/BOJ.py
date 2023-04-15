import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque

check = [False for __ in range(101)]
arr = [[] for __ in range(101)]

def bfs(start)->int:
    que=Queue()
    que.put(start)
    check[start] = True  
    cnt = 0
    while not que.empty():
        cur = que.get()
        for nxt in arr[cur]:
            if not check[nxt]:
                check[nxt] = True
                que.put(nxt)
                
    return cnt
            

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    for i in range(n): 
        a,b = map(int,sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    print(bfs(1))
