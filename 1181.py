from sys import stdin as s
from functools import cmp_to_key


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    a = set([])
    for i in range(n):
        a.add(s.readline())
    
    a = list(a)
        
    a.sort(key = len)
    for i in a:
        print(i[:len(i)-1])