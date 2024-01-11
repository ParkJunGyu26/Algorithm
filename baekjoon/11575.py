t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    string = list(input())

    for j in range(len(string)):
        num = ord(string[j]) - 65
        num = (num * a) + b
        num %= 26
        string[j] = chr(num + 65)
    
    print(''.join(string))