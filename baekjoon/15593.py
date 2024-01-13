n = int(input())
li = []

for i in range(n):
    x, y = map(int, input().split())
    li.append(x)
    li.append(y)

arr = [0 for i in range(max(li))]

for i in range(0, len(li), 2):
    for j in range(li[i], li[i+1]):
        arr[j] += 1

ans = []

for i in range(0, len(li), 2):
    sum = 0
    for j in range(li[i], li[i+1]):
        arr[j] -= 1
    for k in arr:
        if k != 0:
            sum += 1        
    ans.append(sum)

    for j in range(li[i], li[i+1]):
        arr[j] += 1
    
print(max(ans))