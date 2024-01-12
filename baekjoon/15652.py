from itertools import combinations_with_replacement as cbwr

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for x in cbwr(arr, m):
    print(' '.join(map(str, x)))