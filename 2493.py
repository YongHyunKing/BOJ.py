from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue



if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    li = list(map(int,s.readline().split()))
    ans = [0 for __ in range(n)]
    stack1,stack2 = [], []
    for i in range(len(li)):
        stack1.append([li[i],i])
        
    while len(stack1)!=0:
        if len(stack2)==0:
            stack2.append(stack1.pop())
        else:
            while len(stack2)!=0:
                if stack2[-1][0]<stack1[-1][0]:
                    ans[stack2[-1][1]]=stack1[-1][1]+1
                    stack2.pop()
                else: break

            stack2.append(stack1.pop())
            
    while len(stack2)!=0:
        ans[stack2[-1][1]]=0
        stack2.pop()
                
    for i in ans:
        print(i,end=" ")
        

    
    
        
