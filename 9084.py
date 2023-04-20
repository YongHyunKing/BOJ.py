import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop



if __name__ == "__main__":
    #sys.stdin = open('input.txt', 'rt')
    t = int(sys.stdin.readline())
    
    for i in range(t):
        n = int(sys.stdin.readline())
        coin = list(map(int,sys.stdin.readline().rstrip().split()))
        num = int(sys.stdin.readline())
        dp = [0 for __ in range(num+1)]
        cnt = [0 for __ in range(num+1)]
        
        dp[0] = 1
            
        
        for j in range(n):
            for k in range(coin[j],num+1):
                dp[k] += dp[k-coin[j]]

        print(dp[num])