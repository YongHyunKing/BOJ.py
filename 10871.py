from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n,x = map(int,s.readline().split());
    a = map(int,s.readline().split());
    for num in a:
        if num < x:
            print(num,end=' ')