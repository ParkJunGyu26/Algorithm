n = int(input())
dp = [0] * 1000001
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[n])