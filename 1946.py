import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    t = int(sys.stdin.readline())
    
    for i in range(t):
        arr = []
        n = int(sys.stdin.readline())
        for j in range(n):
            arr.append(list(map(int,sys.stdin.readline().split())))
        
        arr.sort() 
        ans = 1
        second = arr[0][1]
        for f,s in arr:
            if s < second :
                ans +=1
                second = s
        print(ans)

