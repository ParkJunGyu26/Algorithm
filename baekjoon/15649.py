from itertools import permutations as pm

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for i in pm(arr, m):
    print(' '.join(map(str, i)))