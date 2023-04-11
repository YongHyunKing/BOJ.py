from sys import stdin as s
from typing import Sequence, MutableSequence





if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr = list(map(int,s.readline().split()))
    ans = []
    ans.append(arr[0])
    
    for i in range(1,len(arr)):
        num = arr[i]
        if num>ans[len(ans)-1]:
            ans.append(num)
        else:
            left,right=0, len(ans)-1

            tmp_mid = -1
            while left<=right:
                mid = (left+right)//2
                if ans[mid] < num:
                    left = mid + 1
                else:
                    tmp_mid = mid
                    right = mid - 1
            ans[tmp_mid] = num
         
    print(len(ans))
    # print(sum(ans))
