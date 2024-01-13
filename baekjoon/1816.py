import math

n = int(input())
for i in range(n):
    s = int(input())
    check = True
    for j in range(2, 1000001):
        if s % j == 0:
            check = False
            break
    if (check == True):
        print("YES")
    else:
        print("NO")