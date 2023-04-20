import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop

in_cnt = []
arr = []
ans = []
check = []

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    arr = [[] for __ in range(n+1)]
    in_cnt = [0 for __ in range(n+1)]
    check = [False for __ in range(n+1)]
    
    for s in range(1,n+1):
        tmp = sys.stdin.readline()
        for e in range(n):
            if tmp[e] == '1' : 
                arr[e+1].append(s)
                in_cnt[s]+=1
                
    que = []
                
    for i in range(1,n+1):
        if in_cnt[i] == 0: heappush(que,-i)

    # 답 넣기 + arr[i] 정렬(사전 순으로 출력을 위해) + in_cnt 체크
    flag = False
    for i in range(0,n+1) :
        ans.append(i)
        if i!=0 and in_cnt[i] == 0 : flag = True
    
    if not flag :
        print(-1)
        sys.exit()
                
    
    
    while que :
        cur = -heappop(que)
        ans[cur] = n
        for nxt in arr[cur]:
            in_cnt[nxt] -= 1
            if in_cnt[nxt] == 0 : heappush(que,-nxt)
            
        n-=1
        

    print(*ans[1:])

