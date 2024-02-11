bar = input()

ans = 0 # 최종 답
cnt = 0 # 레이저 만날 때마다 추가해주기
tmp = []

for i in bar:
    if i == '(':
        tmp.append(i)
        cnt += 1
        check = True
    else:
        if check == True:   # 직전이 '(' 일 경우
            check = False
            cnt -= 1
            ans += cnt
        else:               # 직전이 ')'일 경우
            cnt -= 1
            ans += 1

print(ans)