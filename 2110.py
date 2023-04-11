from sys import stdin as s
from typing import Sequence, MutableSequence

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,c = map(int,s.readline().split())
    arr = list(map(int,s.readlines()))
    arr.sort()
    left, right = 0, 1000000000
    ans = 0
    
    while left<=right:
        mid = (left + right)//2
        tmp, cnt = 0,1
        for i in range(1,len(arr)):
            tmp += (arr[i]-arr[i-1])
            if tmp >=mid:
                cnt+=1
                tmp=0
        
        if cnt>=c:
            ans = mid
            left = mid + 1
        else : right = mid - 1
        
    print(ans)
