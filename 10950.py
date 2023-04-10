from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    
    for i in range(n):
        a, b = map(int,s.readline().split())
        print(a+b)