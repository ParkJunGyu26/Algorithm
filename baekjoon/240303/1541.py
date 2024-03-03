# 그리디 알고리즘 (-가 나오면 그 뒤에 값들은 괄호 해주면 될듯)
import sys
input = sys.stdin.readline

math_sentence = list(input())
tmp = ''
sorted_input = []
for i in math_sentence:
    if i != '+' and i != '-':
        tmp += i
    else:
        sorted_input.append(int(tmp))
        tmp = ''
        sorted_input.append(i)
sorted_input.append(int(tmp))

minus_sorted = []
minus_check = False
cnt = 0
minus_cnt = 0
for i in sorted_input:
    if i == '+':
        continue

    if i == '-':
        cnt -= minus_cnt
        minus_cnt = 0
        minus_check = True
        continue
    
    if minus_check == True:
        minus_cnt += i
    else:
        cnt += i

if minus_cnt == 0:
    print(cnt)
else:
    print(cnt-minus_cnt)