import sys
sys.stdin = open('input.txt', 'rt')
N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(N_list)
result = 0
while start <= end:

    mid = (start + end) // 2
    cnt = 0
    for i in N_list:
        if i > mid:
            cnt += (i - mid)
        if cnt > M:
            break

    if cnt > M:
        result = mid
        start = mid + 1
    elif cnt == M:
        result = mid
        break
    else:
        end = mid - 1
print(result)