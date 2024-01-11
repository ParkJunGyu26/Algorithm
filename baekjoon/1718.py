string = list(input())      # 평문
key = list(input())         # 암호키

for i in range(len(key)):
    key[i] = ord(key[i]) - 96

for i in range(len(string)):
    if 96 < ord(string[i]) < 123:
        num = ord(string[i]) - 97
        num = num - key[i%len(key)]
        num %= 26
        string[i] = chr(num + 97)

print(''.join(string))