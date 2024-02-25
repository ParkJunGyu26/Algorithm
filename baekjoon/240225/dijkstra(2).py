import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)  # 무한대(10억)

# n = 노드 개수, m = edge(간선) 개수
n, m = map(int, input().split())
start = int(input())    # 시작 노드 번호

# 노드가 1번부터 시작하므로 n+1
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# a = 시작점, b = 도착점, c = 간선 가중치
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 우선순위 큐를 이용한 다익스트라
def dijkstra(start):
    q = []
    heappush(q, (0, start))
    # 시작 노드 번호의 거리는 0으로 초기화
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        # 방문한 적이 있다면 패스
        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            cost = distance[now] + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("방문할 수 없는 노드입니다.")
    else:
        print(distance[i])