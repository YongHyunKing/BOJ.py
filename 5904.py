import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop
flag = False
S = []

def recur(a,k):
    if k == 0:
        if a == 1: return 'm'
        return 'o'
    
    if a<=S[k-1] : return recur(a,k-1)
    
    a-=S[k-1]
    if a <= (k+3) : 
        if a==1 : return 'm'
        return 'o'
    
    return(recur(a-(k+3),k))

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    a = int(sys.stdin.readline())
    k = 1
    n = 3
    S.append(3)
    
    while n<=10**9:
        S.append(S[k-1]*2+k+3)
        n+=S[k]
        k+=1
    print(recur(a,len(S)))
