import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

arr = []
oper = []
num = []
maax = -sys.maxsize
miin = sys.maxsize
n = None


def dfs(idx):
    global maax,miin
    if idx == n-1:
        tmp = num[0]
        for i in range(n-1):
            if arr[i] == 0: tmp +=num[i+1]
            elif arr[i] == 1: tmp -=num[i+1]
            elif arr[i] == 2: tmp *=num[i+1]
            else :
                if tmp < 0 and num[i+1]>0 : tmp = int(-(-tmp // num[i+1]))
                else : tmp = int(tmp//num[i+1])
        maax = max(maax,tmp)
        miin = min(miin,tmp)
                
    
    for i in range(4):
        if oper[i] > 0:
            oper[i]-=1
            arr.append(i)
            dfs(idx+1)
            arr.pop()
            oper[i]+=1
        

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    # arr = [[] for __ in range(n-1+4)]
    num = list(map(int,sys.stdin.readline().rstrip().split()))
    oper = list(map(int,sys.stdin.readline().rstrip().split()))
            
    dfs(0)
    print(maax)
    print(miin)
