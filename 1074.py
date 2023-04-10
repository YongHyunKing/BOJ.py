from sys import stdin as s

def recur(y,x,size):
    global cnt,r,c
    if size==1:
        cnt+=1
        if r == y and c == x:
            print(cnt)
        return
        
    nxt = int(size//2)
    if r < y+nxt and c < x+nxt:
        recur(y,x,nxt) # 왼쪽 위
    elif  r < y+nxt and nxt <= x+c:
        cnt+=nxt**2
        recur(y,x+nxt,nxt) #오른쪽 위
    elif nxt <= y+r and c < x+nxt:
        cnt+=(nxt**2)*2
        recur(y+nxt,x,nxt) # 왼쪽 아래
    else:
        cnt+=(nxt**2)*3
        recur(y+nxt,x+nxt,nxt) # 오른쪽 아래

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,r,c = map(int,s.readline().split())
    cnt = -1

    recur(0,0,2**n)
