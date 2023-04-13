from sys import stdin as s
from typing import Sequence, MutableSequence

def cal(arr1, arr2,div):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)): 
        lists = []
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])): 
                answer[i][j] += (arr1[i][k] * arr2[k][j])%div
    return answer

def recur(a : Sequence, cnt : int,div : int)->Sequence:
    if cnt == 1:
        return a
    
    b = recur(a,cnt//2,div)
    b = cal(b,b,div)
    
    if cnt%2==1:
        b = cal(a,b,div)
    
    return b

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,b = map(int,s.readline().split())
    a = []
    for i in range(n):
        a.append(list(map(int,s.readline().split())))
        
    #print(recur(a,b,1000))
    c = recur(a,b,1000)
    for i in c:
        for j in i:
            print(j%1000,end=" ")
        print()
    
    
    
