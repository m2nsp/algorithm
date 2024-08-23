import sys
import heapq

input = sys.stdin.readline

N = int(input())                                # N : 정점의 개수
M = int(input())                                # M : 간선의 개수
myList = [[] for _ in range(N+1)]               # 정점에 연결된 간선 정보 저장할 리스트
dist = [sys.maxsize] * (N + 1)                  # 거리 정보 저장할 리스트

for _ in range(M):                              # 간선 정보 저장
    start, end, weight = map(int, input().split())
    myList[start].append((end, weight))
    
start_index, end_index = map(int, input().split())        # 시작, 끝 정점 입력

def dijkstra(start, end):                        # 다익스트라 알고리즘 수행하는 함수
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0
    
    while pq:                                    # 현재 최단 거리가 가장 짧은 정점을 꺼냄
        current_dist, now = heapq.heappop(pq)
        
        if current_dist > dist[now]:             # 현재 정점까지의 거리가 이미 계산된 거리보다 큰 경우
            continue
        
        for next_node, weight in myList[now]:    # 모든 이웃 정점 확인
            new_dist = current_dist + weight
            if new_dist < dist[next_node]:       # 새로운 거리가 더 짧으면 갱신
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    return dist[end] if dist[end] != sys.maxsize else "INF"    # 목표 정점까지의 최단거리 반환, 도달 못하면 = "INF"

print(dijkstra(start_index, end_index))
