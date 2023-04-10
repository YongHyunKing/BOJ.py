from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a = int(s.readline())
    b = int(s.readline())
    tmp_b = b;
    
    while tmp_b != 0:
        print(a*(tmp_b%10))
        tmp_b = int(tmp_b/10)
    
    print(a*b)
