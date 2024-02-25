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
            cost = distance[now] + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))
    
    return distance

n, m, goal = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

max_time = 0
back_distance = dijkstra(goal)

for i in range(1, n+1):
    if i == goal:
        continue
    go_distance = dijkstra(i)
    count_time = back_distance[i] + go_distance[goal]
    max_time = max(max_time, count_time)

print(max_time)