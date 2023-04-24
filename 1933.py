import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from heapq import heappush, heappop
from functools import cmp_to_key

    
        

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    n = int(sys.stdin.readline())
    pq = []
    arr = []
    end = [0] * n
    height = [0]*n
    check = set()
    for i in range(n):
        s,h,e = map(int,sys.stdin.readline().split())
        arr.append([s,True,i])
        arr.append([e,False,i])
        height[i] = h
        end[i] = e
    
    # 첫번째 우선순위 : 시점이 앞서는지
    # 두번째 우선순위 : 시점이 같다면 시작점인지
    # 세번째 우선순위 : 시점도 같고 둘 다 시작점이면 높이가 더 높은지
    arr.sort(key = lambda x :(x[0],-x[1],-height[x[2]]))
    
    ans = []
    
    now = 0
    for i in range(len(arr)):
        x, start,idx = arr[i]
        if start :
            # 같은 높이 시작점 뒤로 오는거 제거
            if not pq or height[idx] > now :
                now = height[idx]
                ans.append(x)
                ans.append(height[idx])
            heappush(pq,[-height[idx],end[idx]])
        else :
            check.add(x)
            while pq:
                if pq[0][1] not in check: break
                heappop(pq)
            # 같은 높이 끝나는 점 뒤로 오는거 제거
            if not pq and now:
                # 이 부분
                now = 0
                ans.append(x)
                ans.append(0)
            # 높이가 낮아지면서 갱신되는 경우
            elif pq and -pq[0][0] != now:
                now = -pq[0][0]
                ans.append(x)
                ans.append(now)


    print(*ans)
