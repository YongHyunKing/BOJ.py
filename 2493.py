from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue



if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    li = list(map(int,s.readline().split()))
    ans = [0 for __ in range(n)]
    stack = []
    
    for i in range(len(li)):
        while stack and stack[-1][0]<li[i]: stack.pop()
        if stack : ans[i] = stack[-1][1]
        stack.append([li[i],i+1])
        
    print(*ans)
