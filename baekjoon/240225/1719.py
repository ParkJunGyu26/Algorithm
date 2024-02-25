import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)
n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    c = 1
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            cost = distance[now] + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))

dijkstra(start)

if k not in distance:
    print(-1)
else:
    ans = list(filter(lambda x: distance[x] == k, range(len(distance))))
    ans.sort()
    for i in ans:
        print(i)