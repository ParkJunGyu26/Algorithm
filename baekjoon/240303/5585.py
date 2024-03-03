# 그리디 알고리즘
import sys
input = sys.stdin.readline

money = 1000 - int(input())
cnt = 0

while (money > 0):
    ans = 0
    if (money >= 500):
        ans += money // 500
        money -= 500 * ans
    elif (money >= 100): 
        ans += money // 100
        money -= 100 * ans
    elif (money >= 50):
        ans += money // 50
        money -= 50 * ans
    elif (money >= 10):
        ans += money // 10
        money -= 10 * ans
    elif (money >= 5):
        ans += money // 5
        money -= 5 * ans
    else:
        ans += money // 1
        money -= 1 * ans
    cnt += ans

print(cnt)