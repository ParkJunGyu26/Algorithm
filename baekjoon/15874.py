k, length = map(int, input().split())
k %= 26

s = list(input())

for i in range(length):
    # 문자를 숫자로 변환
    x = ord(s[i])

    # 대문자, 소문자에 맞는 숫자들로 바꿔주기
    if 65 <= x <= 90 or 97 <= x <= 122:
        if s[i].isupper(): x -= 65
        else: x -= 97

        # 얼만큼 옮긴 것인지 추가
        x += k

        # 알파벳 개수만큼 나눠주기
        x %= 26

        # 대문자, 소문자에 맞는 숫자들로 바꿔주기
        if s[i].islower() : x += 97
        else: x += 65

        # 문자로 변환
        s[i] = chr(x)

print(''.join(s))