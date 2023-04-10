from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    
    for i in range(n):
        a = s.readline();
        sc = 1
        total = 0
        for j in a:
            if j == 'O':
                total+=sc
                sc+=1
            else:
                sc = 1;
        print(total)