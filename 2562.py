from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a = []
    for i in range(9):
        a.append(int(s.readline()))
    print(max(a))
    print(a.index(max(a))+1)