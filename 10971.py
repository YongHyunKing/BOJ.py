from sys import stdin as s
import sys

def dfs(cur,total,depth):
    global arr, n, ans, start, check
    for nxt in range(n):
        if arr[cur][nxt]!=0 and not check[nxt]:
            check[nxt] = True
            dfs(nxt,total+arr[cur][nxt],depth+1)
            check[nxt] = False

    if depth == n-1 and cur != start and arr[cur][start]!=0:
        ans = min(ans, total+arr[cur][start])
        

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr = []
    ans = sys.maxsize

    check = [False for __ in range(n)]
    for i in range(n):
        arr.append(list(map(int,s.readline().split())))
        
    check[0] = True
    start = 0
    dfs(0,0,0)

    
    # for i in range(n):
    #     check[i] = True
    #     start = i
    #     dfs(i,0)
    #     check[i] = False
    print(ans)