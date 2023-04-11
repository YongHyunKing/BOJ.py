from sys import stdin as s
from typing import Sequence, MutableSequence




if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,m = map(int,s.readline().split())
    arr = list(map(int,s.readline().split()))
    left,right = 0, 1000000000
    height=0
    
    while left<=right:
        mid = (left+right)//2
        tmp = 0
        for i in arr:
            if i - mid>0:
                tmp+=(i-mid)
        
        if tmp < m: right = mid - 1
        else : 
            height = mid
            left = mid +1
        
    print(height)
