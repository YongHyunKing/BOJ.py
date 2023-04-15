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
    n,m = map(int,sys.stdin.readline().split())
    
    for i in range(n+1): parent.append(i)
    
    for i in range(m):
        u,v = map(int,sys.stdin.readline().split())
        parent_u = find_parent(u)
        parent_v = find_parent(v)
        if parent_u != parent_v:
            parent[parent_v] = parent_u
            n-=1
    print(n)