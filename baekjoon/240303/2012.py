# 그리디 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
expected = []
for _ in range(n):
    expected.append(int(input()))

# 정렬
expected.sort()

# 불만족
ans = 0
for i in range(1, n+1):
    ans += abs(i - expected[i-1])
print(ans)