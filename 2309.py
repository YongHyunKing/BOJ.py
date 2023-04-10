from sys import stdin as s


def cal(idx,cnt,total):

    global flag, check, arr,n
    if cnt == 7:
        if total == 100:
            ans = []
            for i in range(len(check)):
                if check[i] :
                    ans.append(arr[i])
            ans.sort()
            for i in ans:
                print(i) 
            flag = True

    if flag or idx == n:
        return
    
    check[idx] = True;
    cal(idx+1,cnt+1,total+arr[idx])
    check[idx] = False
    cal(idx+1,cnt,total)


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = 9
    arr = []
    check = [False for __ in range(n)]
    flag = False
    for i in range(n):
        arr.append(int(s.readline()))

    cal(0,0,0)
        