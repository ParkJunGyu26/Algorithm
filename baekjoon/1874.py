count = 1
ans = []    # '+', '-'를 담을 배열
li = []     # 숫자들을 담을 배열
flag = True

n = int(input())

for i in range(n):
    num = int(input())

    while (num >= count):
        li.append(count)
        ans.append('+')
        count += 1
    if li[-1] == num:
        li.pop()
        ans.append('-')
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for i in ans:
        print(i)