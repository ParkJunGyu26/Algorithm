from itertools import permutations as pm

n = int(input())
li = []

for i in range(1, n+1):
    li.append(i)

for i in pm(li, n):
    print(' '.join(map(str, i)))