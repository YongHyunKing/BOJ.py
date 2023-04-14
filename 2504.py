from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key
import sys

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    string = s.readline().rstrip()
    # print(string)
    stack=[]
    ans = 0
    cnt=0
    
    for i in string:
        # print(stack)
        flag = False
        if len(stack)==0:
            if i==')' or i==']':
                print(0)
                sys.exit()
            stack.append(i)
        else:
            tmp = 0
            while len(stack)!=0:
                if i==']':
                    if stack[-1]=='[':
                        stack.pop()
                        if tmp == 0: stack.append(3)
                        else: stack.append(3*tmp)
                        break
                    elif stack[-1]=='(' or stack[-1]==']':
                        print(0)
                        sys.exit()
                    else:
                        tmp+=stack.pop()
                elif i==')':
                    if stack[-1]=='(':
                        stack.pop()
                        if tmp == 0: stack.append(2)
                        else: stack.append(2*tmp)
                        break
                    elif stack[-1]=='[' or stack[-1]==')':
                        print(0)
                        sys.exit()
                    else:
                        tmp+=stack.pop()
                else:
                    stack.append(i)
                    break
        if  stack[0]!='['and stack[0]!=']' and stack[0]!='(' and stack[0]!=')':
            while len(stack)!=0:
                ans+=stack.pop()      

    # for i in stack:
    #     if i=='['or i==']' or i=='(' or i==')':
    #         print(0)
    #         sys.exit()
    #     else : ans+=i
    print(ans)
                        
                        

