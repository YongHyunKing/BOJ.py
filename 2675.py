from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    for i in range(n):
        a , b = s.readline().split()
        for x in b:
            for i in range(int(a)):
                print(x,end="")
        print()
   