import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    s = sys.stdin.readline().rstrip()

    tmp = ""
    for i in s:
        if i !='+' and i!='-':
            tmp+=i
        else:
            arr.append(int(tmp))
            tmp=""
            arr.append(i)
    arr.append(int(tmp))
    plus = 0
    minus = 0
    flag = False
    
    for i in arr:
        if i == '-': flag = True
        elif i == '+': continue
        elif not flag: plus+=i
        else : minus+=i
    
    print(plus-minus)

