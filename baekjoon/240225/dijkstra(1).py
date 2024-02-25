import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하며, 10억

n, m = map(int, input().split())
start = int(input())
# 1번 노드부터 시작하므로 n+1 으로 해준다.
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

# a는 시작점, b는 도착점, c는 엣지 가중치
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 최단거리 테이블에서 거리가 가장 짧은 노드 탐색(heapq 없을 경우)
def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작하는 노드는 엣지가 0일 것이고, 방문했으므로 True
    distance[start] = 0
    visited[start] = True
    for b, c in graph[start]:
        distance[b] = c

    # 출발 노드 제외한 나머지 노드이므로 n-1
    for _ in range(n-1):
        
        # 방문하지 않은 노드 중에서 가장 작은 값 조회
        now = get_smallest_node()
        visited[now] = True

        # 일반적으로 다익스트라 배우는 이론 부분
        # 해당 노드에 방문하기 위한 최단 거리 계산
        for b, c in graph[now]:
            distance[b] = min(distance[b], distance[now] + c)
        
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("방문하지 않은 노드이므로 infinity")
    else:
        print(distance[i])