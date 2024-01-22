def go(arr):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if i not in arr:
            # go(arr+[i])
            arr.append(i)
            go(arr)
            arr.pop()

n, m = map(int, input().split())
go([])