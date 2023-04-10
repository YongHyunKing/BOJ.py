from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')

    score = int(s.readline())

    if score < 60:
        print("F")
    elif score < 70:
        print("D")
    elif score < 80:
        print("C")
    elif score < 90:
        print("B")
    else :
        print("A")