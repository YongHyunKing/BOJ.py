from sys import stdin as s
from typing import Sequence, MutableSequence

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)): 
        lists = []
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,b = map(int,s.readline().split())
    a = []
    for i in n:
        a.append(list(map(int,s.readline().split())))
    
    
    
