from sys import stdin as s


def cal(idx)->None:
    global check, arr,tmp,ans, n
    if len(tmp) == n:
        total=0
        for i in range(0,n-1):
            total+=abs(int(tmp[i] - tmp[i+1]))
        ans = max(ans,total)
    if idx == n:
        return
    
    for i in range(n):
        if not check[i]:
            tmp.append(arr[i])
            check[i] = True
            cal(idx+1)
            tmp.pop()
            check[i] = False
            
   
        
    
    

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    arr,tmp=[],[]
    ans = 0
    check = [False for __ in range(n)]
    arr = list(map(int,s.readline().split()))
    
    
    cal(0)
    print(ans)
    
    
