import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')

    n, k = map(int, sys.stdin.readline().split())
    arr= list(map(int,sys.stdin.readline().split()))
    plug = [-1]*(n)
    cnt = 0
    ans = 0
    
    
    for i in range(k):
        flag = False
        
        for j in range(n):
            if plug[j]== arr[i]: 
                flag = True
                break
        
        if flag : continue
        
        for j in range(n):
            if plug[j]== -1: 
                plug[j] = arr[i]
                flag = True
                break
            
        if flag : continue

        plug_idx = 0
        arr_idx = 0
        
        for j in range(n):
            tmp = k + 1
            for w in range(i+1, k):
                if plug[j] == arr[w]:
                    tmp = w
                    break
                
            if tmp > arr_idx:
                arr_idx = tmp
                plug_idx = j
            
        ans+=1
        plug[plug_idx] = arr[i]
        
    print(ans)
