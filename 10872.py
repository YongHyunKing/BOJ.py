from sys import stdin as s

def factorial(num : int)->int:
    if num == 0 or num == 1:
        return 1
    return num*factorial(num-1)

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    num = int(s.readline())
    print(factorial(num))