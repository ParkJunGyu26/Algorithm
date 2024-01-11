n = int(input())
li = []

for i in range(1, n+1):
    s, c, l = map(int,input().split())
    li.append([i, s, c, l])

sort_li = sorted(li, key = lambda x : [-x[1], x[2], x[3]])

print(sort_li[0][0])