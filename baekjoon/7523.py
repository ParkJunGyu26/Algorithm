t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())
    minus, plus, sum = 0, 0, 0

    plus = (m * (m+1)) // 2

    if n < 0:
        minus = (n * (n-1)) // 2
    
    sum = plus - minus
    
    print("Scenario #{}:".format(i))
    print(sum)
    print()