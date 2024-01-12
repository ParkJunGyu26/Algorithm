from collections import deque 

s = input()
ans = ''
dq = deque()

check = False

for i in range(len(s)):
    #  공백이거나 '<' 일 때는 그냥 출력
    if s[i] == ' ':
        if len(dq) > 0:
            ans += ''.join(dq)
            ans += ' '
            dq = deque()
        else:
            ans += s[i]
        continue
    elif s[i] == '<':
        check = True
        if len(dq) > 0:
            ans += ''.join(dq)
            ans += s[i]
            dq = deque()
        else:
            ans += s[i]
    elif s[i] == '>':
        check = False
        ans += s[i]

    if check == False:
        if s[i] == '>':
            continue
        else:
            dq.appendleft(s[i])
    elif check == True:
        if s[i] == '<':
            continue
        else:
            ans += s[i]
    
    if i == len(s)-1 and len(dq) > 0:
        ans += ''.join(dq)

print(ans)