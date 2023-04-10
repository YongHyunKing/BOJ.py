from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    year = int(s.readline())

    if (year%4==0 and year%100!=0) or year%400==0:
        print(1)
    else:
        print(0)
