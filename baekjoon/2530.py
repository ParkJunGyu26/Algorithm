h, m, s = map(int, input().split())
time = int(input())

sum = (h * 3600 + m * 60 + s + time) % 86400
h = sum // 3600
m = (sum % 3600) // 60
s = ((sum % 3600) % 60)

print(h, m, s)