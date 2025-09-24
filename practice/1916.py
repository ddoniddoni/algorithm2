import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

start, end = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        print(dist, now)
        if distance[now] < dist:
            continue
        
        for nxt, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))
dijkstra(start)
print(distance[end])