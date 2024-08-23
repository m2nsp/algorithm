import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
myList = [[] for _ in range(N+1)]
dist = [sys.maxsize] * (N + 1)

for _ in range(M):
    start, end, weight = map(int, input().split())
    myList[start].append((end, weight))
    
start_index, end_index = map(int, input().split())

def dijkstra(start, end):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0
    
    while pq:
        current_dist, now = heapq.heappop(pq)
        
        if current_dist > dist[now]:
            continue
        
        for next_node, weight in myList[now]:
            new_dist = current_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    return dist[end] if dist[end] != sys.maxsize else "INF"

print(dijkstra(start_index, end_index))
