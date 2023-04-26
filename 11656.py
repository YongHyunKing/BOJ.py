import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    ans = []
    s = sys.stdin.readline().rstrip()
    tmp = ""
    for i in range(len(s)-1,-1,-1):
        tmp+=s[i]
        ans.append(tmp[::-1])
    
    ans.sort()
    
    for i in ans:
        print(i)