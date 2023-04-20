import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    
    dp = [[0 for __ in range(len(s1)+1)] for __ in range(len(s2)+1)]
    
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1] == s1[j-1]: dp[i][j] = dp[i-1][j-1]+1
            else : dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
    print(dp[len(s2)][len(s1)])

