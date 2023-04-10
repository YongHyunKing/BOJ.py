from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a, b =map(int, s.readline().split())
    c, d = 0 ,0
    while a!=0:
        c=c*10+a%10;
        a = int(a/10)
    while b!=0:
        d=d*10+b%10;
        b = int(b/10)
    print(max(c,d))
    