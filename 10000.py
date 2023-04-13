from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key

#False이어야 a가 뒤에거, b가 앞에거
# 1,0 이면 그대로
# -1 이면 바뀜
def compare(a,b):
    # print(a,b)
    if a[0]==b[0]: # 시작 좌표가 같다면
        if a[1]==b[1]: # 둘 다 시작 or 끝이라면
            if a[1]: # 둘 다 시작인 경우
                if a[2]<b[2] : # 반지름이 작은게 나중에
                    return -1
                return 1
            else: #둘다 끝인 경우
                if a[2]>b[2] : # 반지름이 큰게 먼저
                    return -1
                return 1
        if a[1]: #뒤에게 start이면
            return -1
        return 1
            
    if a[0]<b[0]: # x값이 작은거 먼저
        return -1
    return 1

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr = []
    
    for i in range(n):
        x,r = map(int,s.readline().split())
        arr.append([x-r,False,r,i])
        arr.append([x+r,True,r,i])
    
    
    arr.sort(key = cmp_to_key(compare))

    stack = []
    cnt = 1
    for p in arr:
        if p[1]: #끝점이라면
            tmp_r = 0
            while len(stack)!=0:
                if stack[-1][3]!=p[3]:
                    tmp_r+=stack[-1][2]
                    stack.pop()
                else : 
                    stack.pop()
                    break
            if tmp_r == p[2]: cnt+=1
            stack.append(p)
        else:
            stack.append(p)
            cnt+=1
                
    print(cnt)
                
