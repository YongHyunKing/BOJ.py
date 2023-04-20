import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

n,k = [None]*2
arr, cost = [],[]

class node:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
    def __lt__(self,other):
        if self.A == other.A : return self.B > other.B
        
        if self.A > other.B: return True
        return False


def bfs(first):
    pq = []
    cost[first] = 0
    heappush(pq,[0,first])
    while pq:
        # print(pq)
        
        c,cur = heappop(pq)
        c,cur = c,cur
        if cur == 0:
            print(c)
            return
        if cost[cur] != c : continue

        for coin in arr:
            if cur - coin >=0 and cost[cur]+1<cost[cur-coin]:
                cost[cur-coin] = cost[cur]+1
                heappush(pq,[cost[cur-coin],cur-coin])
    
    print(-1)
            
            

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,k = map(int,sys.stdin.readline().split())
    arr = sorted(list(map(int,sys.stdin.readlines())),key = lambda x : -x)
    cost = [sys.maxsize for __ in range(k+1)]
    
    bfs(k)
    # print(cost)

