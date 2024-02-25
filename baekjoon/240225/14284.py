import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0     # 첫 시작 노드는 방문한 걸로 바꾸기
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            # cost 부분이 무방향(양방향)과 단방향의 차이점 중 하나
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# a -> b : c(가중치)
# 문제에서 무방향 그래프라고 했는데...
# 그래서 a -> b & b -> a 둘 다 해줌(양방향)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])