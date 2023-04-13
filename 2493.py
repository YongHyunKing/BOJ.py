from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue



if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    stack = list(map(int,s.readline().split()))
    ans = []
    
    # while len(stack)!=0:
    #     num = stack.pop()
    #     cnt = 1
    #     idx = 0
    #     while len(stack)!=0:
    #         if num >= stack[len(stack)-1]:
    #             stack.pop()
    #             cnt+=1
    #         else : 
    #             idx = len(stack)
    #             break
        
    #     for i in range(cnt):
    #         ans.append(idx)
            
    # for i in range(len(ans)-1,-1,-1):
    #     print(ans[i],end=" ")
        
