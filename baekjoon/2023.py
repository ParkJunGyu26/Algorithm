from collections import deque
import math

n = int(input())

# for i in range(10**(n-1), 10**n):
#     check = False
#     num_list = list(str(i))
#     num_string = ''.join(num_list)
#     cnt = 0

#     for j in range(len(num_string)):
#         for k in range(2, int(math.sqrt(int(num_string[0:j+1]))) + 1):
#             if i % k == 0:
#                 cnt += 1
    
#     if i != 1 and cnt == 0:
#         print(num_string)
dq = deque()
for i in range(n):
    # n이 1일 때
    if len(dq) == 0:
        dq.append(2)
        dq.append(3)
        dq.append(5)
        dq.append(7)

    # n이 1보다 클 때
    else:
        check = False
        cnt = len(dq)
        
        for j in range(cnt):
            for k in range(1, 10):
                target_num = int(str(dq[j]) + str(k))
                sum = 0

                for h in range(2, int(math.sqrt(target_num)) +1):
                    if target_num % h == 0:
                        sum += 1

                if sum == 0:
                    dq.append(target_num)

        for j in range(cnt):
            dq.popleft()

for i in dq:
    print(i)