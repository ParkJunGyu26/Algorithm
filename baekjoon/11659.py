import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
# arr = [*map(int, input().split())]

prefix_sum = [0] + arr

for i in range(1, n+1):
    prefix_sum[i] += prefix_sum[i-1]

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])