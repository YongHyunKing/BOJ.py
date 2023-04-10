from sys import stdin as s
import math

def check(num : int)->bool:
    
    str_num = str(num)
    diff = int(int(str_num[0]) - int(str_num[1]))
    for i in range(len(str_num)-1):
        if int(int(str_num[i]) - int(str_num[i+1])) != diff:
            return False

    return True

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a = [False for i in range(1001)]
    
    for i in range(100):
        a[i] = True;
    
    for i in range(100,1001):
        a[i] = check(i);
    
    num = int(s.readline());
    ans = 0;
    for i in range(1,num+1):
        if a[i]:
            ans+=1
    print(ans)