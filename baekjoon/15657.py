n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if start == m:
        print(' '.join(map(str, temp)))
        # print(*ans)
        return
    
    for i in range(start, n):
        temp.append(arr[i])
        dfs(i)
        temp.pop()

dfs(0)