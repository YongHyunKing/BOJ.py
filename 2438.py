from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()
