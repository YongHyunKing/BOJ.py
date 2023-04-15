import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque

arr, ans=[],[]
n,m,k = None, None,None

def bfs(start):
    cnt = 0
    check[start]=True
    que = Queue()
    que.put([start,0])
    while not que.empty():
        p = que.get()
        for nxt in arr[p[0]]:
            if not check[nxt]: 
                check[nxt] = True
                if p[1]+1 == k:
                    ans.append(nxt)
                    cnt+=1
                elif p[1]+1 < k:
                    que.put([nxt,p[1]+1])
                
    if cnt == 0: print(-1)
    else :
        ans.sort()
        for i in ans:
            print(i)
    

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,m,k,x = map(int,sys.stdin.readline().split())
    check = [False for __ in range(n+1)]
    arr = [[] for __ in range(n+1)]
    
    
    for i in range(m): 
        a,b = map(int,sys.stdin.readline().split())
        arr[a].append(b)
        
    
    
    bfs(x)
