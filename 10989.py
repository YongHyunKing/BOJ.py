from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    a = [0 for __ in range(10001)]
    
    for i in range(n):
        num = int(s.readline())
        a[num]+=1
        
    for i in range(1,10001):
        for j in range(a[i]):
            print(i)
