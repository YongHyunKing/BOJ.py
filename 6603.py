from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key

def com(idx : int, cnt :int , n :int ,check : MutableSequence,arr : Sequence):
    if cnt == 6:
        tmp = []
        for i in range(1,len(arr)):

            if check[i]:
                tmp.append(arr[i])
        tmp.sort()
        for i in tmp:
            print(i,end=" ")
        print()
        return
    if idx == len(arr):
        return
    
    check[idx] = True
    com(idx+1,cnt+1,n,check,arr)
    check[idx] = False
    com(idx+1,cnt,n,check,arr)


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    while 1:
        arr = list(map(int,s.readline().split()))
        n = arr[0]
        if n == 0: break
        check = [False for __ in range(n+1)]
        com(1,0,n,check,arr)
        print()
