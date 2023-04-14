from sys import stdin as s
from queue import Queue
from collections import deque

# 0 오른쪽
# 1 아래
# 2 왼쪽
# 3 윗쪽

def sim(t : int, nxt : int)->bool:
    global arr,s_y,s_x,d,dy,dx,count,deq
    
    for i in range(t):
        count+=1
        #먼저 움직인다.
        if d == 0 : s_x+=1 # 오
        elif d==1 : s_y+=1 # 아래
        elif d==2 : s_x-=1 # 왼
        else : s_y-=1 # 위
        flag = False
        
        if not (0<s_x<=n and 0<s_y<=n and arr[s_y][s_x]!=2):
            return False
        
        if arr[s_y][s_x] == 1:
            flag = True
        arr[s_y][s_x]=2
        
        de_x.appendleft(s_x)
        de_y.appendleft(s_y)
        if not flag:
            arr[de_y.pop()][de_x.pop()]=0

        
    if nxt == 'D':
        d=(d+1)%4
    else :
        d = (3+d)%4

    return True


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr = [[0 for __ in range(n+1)] for __ in range(n+1)]
    k = int(s.readline())
    s_y,s_x=1,1
    d = 0
    arr[s_y][s_x]=2
    dy,dx = [-1,1,0,0],[0,0,-1,1]
    de_x, de_y=deque(), deque()
    de_y.append(s_y)
    de_x.append(s_x)
    
    que = Queue()
    que.put(0)
    
    for i in range(k):
        a,b = map(int,s.readline().split())
        arr[a][b]=1
    
    count = 0
    tmp_t = 0
    l = int(s.readline())
    end_flag=False
    for i in range(l):
        t,di = s.readline().split()
        t = int(t)
        if not sim(t-que.get(),di):
            end_flag=True
            break
        que.put(t)
    if not end_flag: sim(101,0)
    print(count)