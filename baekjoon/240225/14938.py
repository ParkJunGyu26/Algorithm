import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))
    return distance
    
n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
graph = [[] for i in range(n+1)]

# 양방향이므로 a -> b & b -> a
for i in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

max_item = 0
for i in range(1, n+1):
    start = i
    distance = dijkstra(start)
    count_item = 0
    for j in range(1, len(distance)):
        if distance[j] <= m:
            count_item += item[j]
    max_item = max(max_item, count_item)

print(max_item)