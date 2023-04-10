from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    x, y, w, h = map(int,s.readline().split())
    print(min(x,y,w-x,h-y))
