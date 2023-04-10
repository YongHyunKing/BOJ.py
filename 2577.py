from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    result = [0 for i in range(10)]
    a = int(s.readline())
    b = int(s.readline())
    c = int(s.readline())
    d = a*b*c;
    while d!=0:
        result[d%10]+=1;
        d = int(d/10)
    for num in result:
        print(num)