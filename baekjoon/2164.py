from collections import deque

card = deque([i for i in range(1, int(input()) + 1)])
cnt = 0

while len(card) > 1:
    if cnt == 1:
        cnt = 0
        card.append(card.popleft())
    else:
        card.popleft()
        cnt += 1

print(*card)