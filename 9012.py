from sys import stdin as s
from typing import Sequence, MutableSequence

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    
    for i in range(n):
        stack = []
        string = s.readline()
        for i in string[:len(string)-1]:
            # print(i,end="")
            if i == "(": stack.append(i)
            else : 
                if len(stack)!=0 and stack[len(stack)-1] == "(": stack.pop()
                else : stack.append(i)
            
        if len(stack)==0: print("YES")
        else : print("NO")
