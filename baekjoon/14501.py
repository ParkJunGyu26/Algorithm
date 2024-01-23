n = int(input())

li = []

for i in range(n):
    li.append(list(map(int, input().split())))

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if i + li[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(li[i][1] + dp[i+li[i][0]], dp[i+1])

print(dp[0])