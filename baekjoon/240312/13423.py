import sys
from collections import *

input = sys.stdin.readline

t = int(input())
for _ in range(t):

    # 시간 초과 발생
    # ans = 0
    # n = int(input())
    # arr = list(map(int, input().split()))
    # arr.sort()
    # for i in range(n-2):
    #     for j in range(i+1, n-1):
    #         diff = arr[j] - arr[i]
    #         if (arr[j] + diff) in arr:
    #             ans += 1
    # print(ans)

    n = int(input())
    li = sorted(list(map(int, input().split())))
    spotList = defaultdict(int)
    for i in range(n):
        spotList[li[i]] = 1

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            first = li[i]
            second = li[j]
            third = li[j] + (li[j] - li[i])
            if spotList[third] == 1:
                ans += 1
    
    print(ans)