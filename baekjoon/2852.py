t = int(input())
li = []

for i in range(t):
    team, time = input().split()
    m, s = map(int, time.split(":"))
    time = m * 60 + s
    li.append([team, time])

team_1 , team_2 = 0, 0      # 이긴 횟수 확인
ans_1, ans_2 = 0, 0         # 정답
tmp = []

for i in range(len(li)):
    if li[i][0] == '1':
        team_1 += 1
    else:
        team_2 += 1
    
    if team_1 == team_2:
        if li[i][0] == '2':
            ans_1 += li[i][1] - min(tmp)
        else:
            ans_2 += li[i][1] - min(tmp)
        tmp = []
        team1, team2 = False, False
        continue
    elif team_1 > team_2:
        if li[i][0] == '1':
            tmp.append(li[i][1])
            team1 = True
    else:
        if li[i][0] == '2':
            tmp.append(li[i][1])
            team2 = True
    
    if i == len(li)-1 and len(tmp) > 0:
        if team1:
            ans_1 += 48*60 - min(tmp)
        elif team2:
            ans_2 += 48*60 - min(tmp)

h1, m1 = ans_1 // 60, ans_1 % 60
if h1 < 10:
    h1 = '0' + str(h1)
if m1 < 10:
    m1 = '0' + str(m1)

h2, m2 = ans_2 // 60, ans_2 % 60
if h2 < 10:
    h2 = '0' + str(h2)
if m2 < 10:
    m2 = '0' + str(m2)


print("{}:{}".format(h1, m1))
print("{}:{}".format(h2, m2))