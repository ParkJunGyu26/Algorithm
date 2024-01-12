from itertools import combinations as cb

n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, len(arr)+1):
    for j in cb(arr, i):
        if sum(j) == s: ans += 1

print(ans)

## 아... 크기가 양수네... 난 값이 양수인줄..