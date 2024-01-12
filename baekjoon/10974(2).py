from itertools import permutations as pm

n = int(input())
arr = [i for i in range(n, 0, -1)]

ans = list(pm(arr, n))
ans.sort()

for i in range(len(ans)):
    print(' '.join(map(str, ans[i])))