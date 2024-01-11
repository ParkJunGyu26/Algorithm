input = __import__('sys').stdin.readline

n = int(input())
li = []

for i in range(n):
    command = list(input().split())

    if (command[0] == "top"):
        if (len(li) == 0):
            print(-1)
        else:
            print(li[-1])
    elif (command[0] == "empty"):
        if (len(li) == 0):
            print(1)
        else:
            print(0)
    elif (command[0] == "size"):
        print(len(li))
    elif (command[0] == "pop"):
        if (len(li) == 0):
            print(-1)
        else:
            print(li.pop())
    else:
        li.append(command[1])