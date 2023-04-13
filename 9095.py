from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key

def per(n):
    if n==0:
        return 1
    if n<0:
        return 0
    cnt = 0
    for i in range(1,4):
        cnt+=per(n-i)
        
    return cnt


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    t = int(s.readline())
    
    for i in range(t):
        n = int(s.readline())
        print(per(n))
