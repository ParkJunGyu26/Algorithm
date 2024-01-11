n = int(input())
li = []

for i in range(n):
    string = input()
    li.append(string)

li = list(set(li))

sort_char = sorted(li, key = lambda word: [len(word), word])

for i in sort_char:
    print(i)