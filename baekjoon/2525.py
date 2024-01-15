h, m = map(int, input().split())
time = int(input())

sum = (h * 60 + m + time) % (24*60)
h = sum // 60
m = sum % 60
print(h, m)