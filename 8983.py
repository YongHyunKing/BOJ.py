from sys import stdin as s
from typing import Sequence, MutableSequence

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    m,n,l = map(int,s.readline().split())
    per = list(map(int,s.readline().split()))


    ani = []
    for i in range(n):
        a,b = map(int,s.readline().split())
        ani.append([a,b])
    
    per.sort()
    cnt = 0
    
    for p in ani:
        a,b = p[0], p[1]
        left, right = 0, len(per)-1
        
        while left<=right:
            mid = (left + right)//2
            cal = abs(a-per[mid])+b
            if cal<=l:
                cnt+=1
                break
            elif a > per[mid]:
                left = mid + 1
            else :
                right = mid - 1
                
    print(cnt)