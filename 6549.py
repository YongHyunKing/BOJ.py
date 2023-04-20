from sys import stdin as s
from typing import Sequence, MutableSequence

def find_max(a:Sequence, left : int, mid : int, right : int)->int:
    maax,min_h=arr[mid], arr[mid]
    l,r=mid,mid
    while l!=left or r!=right:
        l_h,r_h=-1,-1
        if l-1>=left: l_h = arr[l-1]
        if r+1<=right : r_h = arr[r+1]
         
        if l_h>r_h:
            l-=1
            min_h = min(min_h,arr[l])
            maax = max(maax, (r-l+1)*min_h)
        else:
            r+=1
            min_h = min(min_h,arr[r])
            maax = max(maax, (r-l+1)*min_h)
        
    return maax

def recur(a: Sequence,left : int, right : int)->int:
    if left == right:
        return a[left]
    
    mid = (left+right)//2
    l_side = recur(a,left,mid)
    r_side = recur(a,mid+1,right)
    both = find_max(a,left,mid,right)
    
    return max(l_side,r_side,both)

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    while 1 :
        arr = list(map(int,s.readline().split()))
        if arr[0] == 0: break
        print(recur(arr,1,len(arr)-1))
        
