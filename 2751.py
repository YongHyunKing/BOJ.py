from sys import stdin as s
from typing import Sequence, MutableSequence

def mergesort(a : MutableSequence)->None:
    def _mergesort(a:MutableSequence, left:int, right:int)->None:
        if left >= right:
            return
        center = (left+right)//2
        
        _mergesort(a,left,center)
        _mergesort(a,center+1,right)
        
        p = j = 0
        i = k = left
        
        while i <= center:
            buff[p] = a[i]
            p+=1
            i+=1
            
        while j < p and i<=right:
            if buff[j]<=a[i]:
                a[k]=buff[j]
                j+=1
            else:
                a[k]=a[i]
                i+=1
            k+=1
        
        while j < p:
            a[k] = buff[j]
            j+=1
            k+=1
    
    
    n = len(a)
    buff = [None]*n
    _mergesort(a,0,n-1)
    
    del buff

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    a = []
    for i in range(n):
        a.append(int(s.readline()))
    
    # mergesort(a)
    a.sort()
    for i in a:
        print(i)
