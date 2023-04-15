import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key

parent = []


def find_parent(idx):
    if idx == parent[idx] : return idx
    parent[idx] = find_parent(parent[idx])
    return parent[idx]
    
if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    v, e = map(int,sys.stdin.readline().split())
    for i in range(v+1): parent.append(i)
    
    edges = []
    for i in range(e):
        a,b,w = map(int,sys.stdin.readline().split())
        edges.append([w,a,b])
    
    edges.sort()
    ans = 0
    for edge in edges :
        w,a,b = edge
        parent_a, parent_b = find_parent(a), find_parent(b)

        if  parent_a != parent_b:
            ans+=w
            parent[parent_b] = parent_a
        
    print(ans)
        

