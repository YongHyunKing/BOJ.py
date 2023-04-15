import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque

def bfs(start)->bool:
    global check, arr
    check[start] = 2
    que = Queue()
    que.put([start,2])
    
    while not que.empty():
        cur,color = que.get()
        for nxt in arr[cur]:
            if check[nxt] == color : return False
            if check[nxt] ==1 :
                check[nxt] = 2 if color == 3 else 3
                que.put([nxt,check[nxt]])
    return True

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    k = int(sys.stdin.readline())

    for i in range(k):
        v,e = map(int,sys.stdin.readline().split())
        check = [0 for __ in range(20001)]
        arr = [[] for __ in range(20001)]
        for j in range(e):
            a, b = map(int,sys.stdin.readline().split())
            check[a],check[b] = 1, 1
            arr[a].append(b)
            arr[b].append(a)
        
        flag = False
        for i in range(len(arr)):
            if flag : break
            if check[i]==1:
                if not bfs(i):
                    print("NO")
                    flag = True
        if not flag : print("YES")
                    
        