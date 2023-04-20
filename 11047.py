import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n,k = map(int, sys.stdin.readline().split())
    coin = list(map(int,sys.stdin.readlines()))
    ans = 0
    a = len(coin)-1
    while k!=0:
        for i in range(a,-1,-1):
            if k-coin[i]>=0:
                ans+=int(k//coin[i])
                k = int(k%coin[i])
                a=i
                break
            
    print(ans)
