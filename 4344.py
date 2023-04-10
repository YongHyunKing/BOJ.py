from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    
    for i in range(n):
        a = list(map(int,s.readline().split()));
        mean = sum(a[1:])/a[0]
        c = list(map(lambda x: 1 if x > mean else 0,a[1:]))
        print(f'{sum(c)/a[0]*100:.3f}%')
        