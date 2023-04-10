from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    garo =[]
    sero = []
    a, b = map(int, s.readline().split())
    n = int(s.readline())
    
    garo.append(a)
    sero.append(b);
    garo.append(0)
    sero.append(0)
    ans = 0;
    
    for i in range(n):
        c, d= map(int,s.readline().split())
        if c == 0:
            sero.append(d)
        else:
            garo.append(d)
    garo.sort()
    sero.sort()
    
    for i in range(len(garo)-1):
        small_garo = int(garo[i+1])-int(garo[i])
        for j in range(len(sero)-1):
            small_sero = int(sero[j+1])-int(sero[j])
            ans = max(ans, int(small_sero*small_garo))
    print(ans)
