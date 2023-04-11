from sys import stdin as s
from typing import Sequence, MutableSequence
import math

def cal_dist(p1,p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

def recur_mid(a : Sequence, min_dist:int)->int:
    # 위에 7개와 비교하여 가장 작은 거리 추출
    for i in range(len(a)):
            for j in range(i+1,i+8):
                if j<len(a):
                    min_dist = min(min_dist,cal_dist(a[i],a[j]))
                
    return min_dist

def recur(a : Sequence,left : int, right : int)->int:
    if right-left == 1: # 점이 2개인 경우
        p1,p2 = a[left], a[right]
        return cal_dist(p1,p2)
    elif right - left == 2: # 점이 3개인 경우
        p1,p2,p3 = a[left], a[left+1], a[right]
        return min(cal_dist(p1,p2),cal_dist(p1,p3),cal_dist(p2,p3))
    
    mid = (left+right)//2
    min_dist = min(recur(a,left,mid),recur(a,mid+1,right))
    
    #min_dist만큼 떨어져 있는 좌표들을 저장
    tmp_arr = []
    
    #l_std는 왼쪽 영역에서 합치는 경계에 맞닿아 있는 값
    #r_std는 오른쪽 영역에서 합치는 경계에 맞닿아 있는 값
    l_std, r_std = a[mid][0],a[mid+1][0]
    for i in range(mid,left-1,-1):
        if abs(a[i][0]-l_std)<=math.sqrt(min_dist):
            tmp_arr.append(a[i])
        else: break
        
    for i in range(mid+1,right+1):
        if abs(a[i][0]-r_std)<=math.sqrt(min_dist):
            tmp_arr.append(a[i])
        else: break
    
    #min_dist안에 들어온 좌표들을 다시 y값으로 정렬
    tmp_arr.sort(key = lambda x : x[1])
    return min(min_dist,recur_mid(tmp_arr,min_dist))


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr = []
    for i in range(n):
        arr.append(list(map(int,s.readline().split())))
    
    arr.sort(key = lambda x : (x[0],x[1]))
    #print(arr)
    
    print(recur(arr,0,len(arr)-1))