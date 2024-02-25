import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)
test = int(input())
for i in range(test):
    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    # a -> b : c 비용
    for j in range(m):
        b, a, c = map(int, input().split())
        graph[a].append((b, c))

    count = 0

    def dijkstra(start):
        global count
        q = []
        # start 노드는 거리가 0
        heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heappop(q)
            # 방문한 적이 있다면 INF 보다 작을테니
            if distance[now] < dist:
                continue

            for b, c in graph[now]:
                cost = distance[now] + c
                if cost < distance[b]:
                    distance[b] = cost
                    heappush(q, (cost, b))
            
            count += 1
    
    dijkstra(start)
    
    max_time = max([i for i in distance if i < INF])
    print(count, max_time)