n = int(input())

    #  0   1  2   3  4  5  6  7  8  9
dp = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]

for i in range(10, n+1):
    dp.append(dp[i-5]+1)

print(dp[n])