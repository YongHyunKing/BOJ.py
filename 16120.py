import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    stack = []
    s = sys.stdin.readline().rstrip()
    
    for i in s :
        stack.append(i)
        while len(stack)>=4:
            if ''.join(stack[-4:]) == 'PPAP': 
                for i in range(3) : stack.pop()
            else : break

        
    if len(stack)==1 and stack[0] == 'P': print("PPAP")
    else : print("NP")