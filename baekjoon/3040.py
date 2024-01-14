li = []

for i in range(9):
    li.append(int(input()))

sum = sum(li)

for i in range(8):
    for j in range(i+1, 9):
        if sum - (li[i] + li[j]) == 100:
            for k in li:
                if k == li[i] or k == li[j]:
                    continue
                print(k)