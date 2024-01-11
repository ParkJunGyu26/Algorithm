s = input()
stack = []
temp = 1
result = 0

# 각 문자를 확인
for i in range(len(s)):
    # 열린 괄호들은 stack에 쌓고 temp 값 변경
    if s[i] == '(':
        temp *= 2
        stack.append('(')
    elif s[i] == '[':
        temp *= 3
        stack.append('[')
    # 닫힌 괄호들은 이전 괄호와 비교
    elif s[i] == ')':
        # stack이 비어있거나 직전 괄호 모양이 다르면
        if not stack or stack[-1] == '[':
            result = 0
            break
        # 쌍을 이루는 괄호일 경우
        elif s[i-1] == '(':
            result += temp
        # temp 초기화
        temp //= 2
        stack.pop()
    # 닫힌 괄호 ] 를 이전 괄호와 비교        
    else:
        # stack이 비어있거나 직전 괄호 모양이 다르면
        if not stack or stack[-1] == '(':
            result = 0
            break
        elif s[i-1] == '[':
            result += temp
        # temp 초기화
        temp //= 3
        stack.pop()

# stack이 비어있지 않은 경우    
if stack:
    result = 0
print(result)