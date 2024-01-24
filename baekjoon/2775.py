t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())

    dp = []
    # dp = [i for i in range(1, n+1)] -> 0층 사람 수
    for j in range(n):
        dp.append(j+1)

    for j in range(k):
        for q in range(n):
            if q == 0:
                continue
            else:
                dp[q] = dp[q] + dp[q-1]
    print(dp[n-1])