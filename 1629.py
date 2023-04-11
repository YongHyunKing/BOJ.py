from sys import stdin as s
from typing import Sequence, MutableSequence

def recur(num:int, cnt: int, div : int)->int:
    if cnt == 1:
        return int(num%div)
    
    mul = recur(num,cnt//2,div)
    mul = int((mul*mul)%div)
    
    if cnt%2==1:
        mul = int((mul*num)%div)
    
    return mul

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a,b,c = map(int,s.readline().split())
    print(recur(a,b,c))