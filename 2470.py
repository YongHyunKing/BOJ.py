from sys import stdin as s
from typing import Sequence, MutableSequence
import sys

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr = list(map(int,s.readline().split()))
    arr.sort()
    
    ans,cur_abs= [0,0], sys.maxsize

    
    for p in arr:
        left,right = 0, len(arr)-1
        while left<=right:
            mid = (left+right)//2
            tmp = p+arr[mid]
            
            if tmp > 0 : right = mid - 1
            else : left = mid + 1
            
            if arr[mid]!=p and abs(tmp) < cur_abs:
                cur_abs = abs(tmp)
                ans = [arr[mid],p]
    
    ans.sort()
    print(ans[0],ans[1])
    
    
