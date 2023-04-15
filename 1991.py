import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key

def pre_order(idx,arr):
    
    print(chr(idx+ord('A')),end="")
    
    if arr[idx][0] != -1 : pre_order(arr[idx][0],arr)
    if arr[idx][1] != -1 : pre_order(arr[idx][1],arr)

def in_order(idx,arr):
    if arr[idx][0] != -1 : in_order(arr[idx][0],arr)
    print(chr(idx+ord('A')),end="")
    if arr[idx][1] != -1 : in_order(arr[idx][1],arr)
    

def post_order(idx,arr):
    if arr[idx][0] != -1 : post_order(arr[idx][0],arr)
    if arr[idx][1] != -1 : post_order(arr[idx][1],arr) 
    print(chr(idx+ord('A')),end="")

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    arr = [[-1,-1]for __ in range(n)]
    for i in range(n):
        s,l,r = sys.stdin.readline().split()
        s = ord(s)-ord('A')
        if l != '.':
            arr[s][0]=ord(l)-ord('A')
        if r != '.':
            arr[s][1] =ord(r)-ord('A')
            
    pre_order(0,arr)
    print()
    in_order(0,arr)
    print()
    post_order(0,arr)