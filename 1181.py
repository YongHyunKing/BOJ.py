from sys import stdin as s
from typing import MutableSequence

# 1. 길이가 짧은거 부터
# 2. 길이가 같으면 사전 순으로

# s2가 s1보다 큰가?
def big(s1:str, s2:str)->bool:
    if len(s1) == len(s2):
        return s1 < s2
    
    return len(s1) < len(s2)

def sort3(a:MutableSequence, idx1:int, idx2: int, idx3:int):
    if not big(a[idx1],a[idx2]) : a[idx2], a[idx1] = a[idx1], a[idx2]
    if not big(a[idx2],a[idx3]) : a[idx2], a[idx3] = a[idx3], a[idx2]
    if not big(a[idx1],a[idx2]) : a[idx2], a[idx1] = a[idx1], a[idx2]
    
    return idx2

def quicksort(a: MutableSequence, left : int, right: int):
    pl, pr = left, right
    m = sort3(a,pl,(pl+pr)//2,pr)
    pivot = a[m]
    
    a[m], a[pr-1] = a[pr-1],a[m]
    
    pl+=1
    pr-=2
    
    while pl<=pr:
        # pl은 큰 거를 찾음
        while not big(pivot,a[pl]) : pl+=1
        while big(pivot,a[pr]) : pr-=1

        if pl <=pr:
            a[pl],a[pr] = a[pr], a[pl]
            pl+=1
            pr-=1       
    
    if left < pr: quicksort(a,left,pr)
    if pl < right: quicksort(a,pl,right)


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    a = set()
    for i in range(n):
        a.add(s.readline())
    
    a = list(a)
    
    quicksort(a,0,len(a)-1)    
    
    for i in a:
        print(i[:len(i)-1])