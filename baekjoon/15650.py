from itertools import combinations as cb

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for t in cb(arr, m):
    print(' '.join(map(str, t)))