import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

small_tree = []
big_tree = []
big = []
small = []
check = []

def small_dfs(num):
    for i in small_tree[num]:
        if not check[i] :
            check[i] = True
            small[i]+=1
            small_dfs(i)
            
def big_dfs(num):
    for i in big_tree[num]:
        if not check[i] :
            check[i] = True
            big[i]+=1
            big_dfs(i)

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n, m = map(int,sys.stdin.readline().rstrip().split())
    
    small_tree = [[] for __ in range(n+1)]
    big_tree = [[] for __ in range(n+1)]
    big = [0 for __ in range(n+1)]
    small = [0 for __ in range(n+1)]
    
    tmp = []
    
    for i in range(m) :
        a  = list(map(int,sys.stdin.readline().rstrip().split()))
        if a not in tmp : tmp.append(a)
    
    for i in tmp :
        big_tree[i[1]].append(i[0])
        small_tree[i[0]].append(i[1])
        
    for i in range(1,n+1):
        check=[False for __ in range(n+1)]
        small_dfs(i)
        check=[False for __ in range(n+1)]
        big_dfs(i)

    ans = 0
    for i in range(1,n+1):
        if big[i]>=int((n+1)//2) or small[i]>=int((n+1)//2):
            ans+=1
    print(ans)