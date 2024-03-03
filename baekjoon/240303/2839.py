# 그리디 알고리즘
import sys
input = sys.stdin.readline

N = int(input())
count = 0

while(N >=3):
    if (N % 5 == 0):
        count += N // 5
        N = 0
        break
    else:
        N -= 3
        count += 1

if (N > 0):
    print(-1)
else:
    print(count)