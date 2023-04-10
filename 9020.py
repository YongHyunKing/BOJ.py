from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a = [False for i in range(10001)];
    a[1]=True
    a[0]=True
    for i in range(2,10001):
        b = 0
        if a[i] == False:
            b=2*i;
            while b<=10000:
                a[b]=True;
                b+=i
    n = int(s.readline())
    
    for i in range(n):
        num = int(s.readline())
        for i in reversed(range(2,int(num/2+1))):
            if not a[i] and not a[num-i]:
                print(i,num-i)
                break;
        
    
