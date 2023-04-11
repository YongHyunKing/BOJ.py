from sys import stdin as s
from typing import Sequence, MutableSequence

def binary_search(a :Sequence,num :int)->None:
    left, right = 0, len(a)-1
    
    while left <= right:
        mid = int((left + right)//2)
        if num < arr[mid]: right = mid - 1
        elif  num > arr[mid] : left = mid + 1
        else : return True
        
    return False
if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr = list(map(int,s.readline().split()))
    arr.sort()
    m = int(s.readline())
    q = list(map(int,s.readline().split()))
    
    for i in q:

        if binary_search(arr,i): print(1)
        else : print(0)
    