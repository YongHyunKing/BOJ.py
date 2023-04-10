from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a = int(s.readline())

    for i in range (1,10):
        print(f'{a} * {i} = {a*i}')