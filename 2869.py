from sys import stdin as s

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    a,b,v = map(int, s.readline().split())
    v-=a;
    
    ans = int(v//(a-b))
    
    if v%(a-b) != 0:
        ans+=1
    
    
    print(ans+1)