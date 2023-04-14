from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,k = map(int,s.readline().split())
    string = s.readline().rstrip()
    stack = []
    
    for i in string:
        while stack and stack[-1]<i and k>0  :
            stack.pop()
            k-=1
        stack.append(i)
    
    print(''.join(stack[:k+len(stack)]))
    
    #시간초과 안남
    # print(''.join(stack[:-k+len(stack)]))
    # ans = ""
    # for i in range(len(stack)-k):
    #     ans+=stack[i]
    # print(ans)
    # ans = 0
    
    #시간초과 남
    # if k >0:
    #     for i in range(len(stack)-k):
    #         ans=ans*10+stack[i]
    # else:
    #     for i in range(len(stack)):
    #         ans=ans*10+stack[i]
    # print(ans)
