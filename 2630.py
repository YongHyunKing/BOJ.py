from sys import stdin as s
from typing import Sequence, MutableSequence

def check(a:Sequence,y:int,x:int,size:int)->bool:
    color = a[y][x]
    for i in range(y,y+size):
        for j in range(x,x+size):
            if a[i][j] != color:
                return False
    return True

def count(a:Sequence,y:int,x:int,size:int):
    global blue, white
    if not check(a,y,x,size):
        nxt = int(size//2)
        if nxt == 0: return
        count(a,y,x,nxt)
        count(a,y+nxt,x,nxt)
        count(a,y,x+nxt,nxt)
        count(a,y+nxt,x+nxt,nxt)
    else :
        if a[y][x] == 0 : white+=1
        else : blue+=1
    


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr = []
    blue = 0
    white = 0
    for i in range(n):
        arr.append(list(map(int,s.readline().split())))
    count(arr,0,0,n)
    print(white)
    print(blue)