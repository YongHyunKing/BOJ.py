from sys import stdin as s
# a = [0, 0, 0]

def hanoi(n,start, via, end):
    if n==1:
        print(start, end)
        return
    
    hanoi(n-1,start,end,via)
    print(start, end)
    hanoi(n-1,via,start,end)
    return

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    num = int(s.readline())
    print(2**num-1)
    if num<=20:

        hanoi(num,1,2,3)