from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a = [False for i in range(2000)];
    a[1]=True
    a[0]=True
    for i in range(2,1001):
        b = 0
        if a[i] == False:
            b=2*i;
            while b<=1000:
                a[b]=True;
                b+=i
    n = int(s.readline())
    l = list(map(int,s.readline().split()))
    ans = 0;
    for i in l:
        if not a[i] :
            ans+=1;
    print(ans)
    
