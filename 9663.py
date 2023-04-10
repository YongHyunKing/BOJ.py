from sys import stdin as s

def cal(x,cnt):
    global ans, n, chess, sero, garo, up, down
    if cnt==n:
        ans+=1
        return
    if x==n:
        return
    
    for y in range(n):
        if not garo[y] and not up[y+x] and not down[y-x+n-1]:
            garo[y]=up[y+x]=down[y-x+n-1]=True
            cal(x+1,cnt+1)
            garo[y]=up[y+x]=down[y-x+n-1]=False
            


if __name__ == "__main__":
    ans = 0
    n = 8

    garo = [False for __ in range(n)]
    up = [False for __ in range(2*n-1)]
    down = [False for __ in range(2*n-1)]       
    cal(0,0)
    print(ans)

