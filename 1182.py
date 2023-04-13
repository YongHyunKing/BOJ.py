from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key

def dfs(idx,tmp):
    global cnt
    if len(tmp)!=0 and sum(tmp) == a:
        cnt+=1
    
    for i in range(idx,n):
        tmp.append(arr[i])
        dfs(i+1,tmp)
        tmp.pop()
        
if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,a = map(int,s.readline().split())
    arr = list(map(int,s.readline().split()))
    cnt = 0
    dfs(0,[])
    print(cnt)
