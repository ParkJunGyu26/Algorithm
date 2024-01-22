n, m = map(int ,input().split())
li = list(map(int, input().split()))

left, right = 0, 1
ans = 0

while (left <= right and right <= n):

    sum_nums = li[left:right]
    cnt = sum(sum_nums)

    if cnt > m:
        left += 1
    elif cnt == m:
        right += 1
        ans += 1
    else:
        right += 1

print(ans)