from sys import stdin as s
from queue import Queue


def bfs(i,j,h)->None:
    global check,arr,dx,dy,n
    q = Queue()
    q.put([i,j])
    
    while not q.empty():
        y,x = q.get()
        for i in range(4):
            nx, ny = dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<n and arr[ny][nx]>h and not check[ny][nx]:
                check[ny][nx] = True
                q.put([ny,nx])
                
    


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    dx, dy = [-1,1,0,0] , [0,0,1,-1]
    arr = []
    ans = 1
    
    max_h = 0

    for i in range(n):
        arr.append(list(map(int,s.readline().split())))
        tmp=max(arr[i])
        max_h = max(max_h,tmp)

    for height in range(max_h)da:
        check =[[False for __ in range(n)] for __ in range(n) ]
        tmp = 0;
        for i in range(n):
            for j in range(n):
                if not check[i][j] and arr[i][j]>height:
                    check[i][j] = True;
                    bfs(i,j,height)
                    tmp+=1
        
        # print(f'height : {height}, tmp : {tmp}')
        ans = max(ans,tmp)

    
    print(ans)