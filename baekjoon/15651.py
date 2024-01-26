n, m = map(int, input().split())
temp = []
li = [i for i in range(1, n+1)]

def dfs(depth):
    if depth == m:
        print(*temp)
        return
    else:
        for i in range(n):
            print("before i : ", i)
            temp.append(li[i])
            dfs(depth + 1)
            temp.pop()
            print("after i : ", i)

dfs(0)