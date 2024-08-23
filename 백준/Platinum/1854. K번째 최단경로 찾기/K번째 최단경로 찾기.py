import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())                                # N: 노드 수, M: 간선 수, K: K번째 최단 경로를 찾기 위한 수

W = [[] for _ in range(N + 1)]                                     # 그래프 초기화
distance = [[sys.maxsize] * K for _ in range(N + 1)]               # 각 노드에서 K번째로 작은 최단거리를 저장할 리스트

for _ in range(M):                                                 # 간선 정보 입력 받음
    a, b, c = map(int, input().split())
    W[a].append((b, c))                                            # 노드 a에서 b로 가는 비용이 c인 간선

pq = [(0, 1)]                                                      # 우선순위 큐 초기화, (비용, 노드)
distance[1][0] = 0                                                 # 시작 노드 (1번 노드)의 첫 번째 최단거리= 0으로 초기화

while pq:                                                          # 다익스트라 알고리즘 이용한 최단거리 계산
    cost, node = heapq.heappop(pq)  
    for nNode, nCost in W[node]:  
        sCost = cost + nCost  
        if distance[nNode][K - 1] > sCost:                        # 새롭게 계산한 누적 비용이 해당 노드의 K번째 최단거리보다 작으면 업데이트
            distance[nNode][K - 1] = sCost 
            distance[nNode].sort()                                # K개의 최단거리를 정렬하여 K번째가 가장 큰 값이 되도록 유지
            heapq.heappush(pq, [sCost, nNode]) 

# 모든 노드에 대해 K번째 최단거리를 출력
for i in range(1, N + 1):
    if distance[i][K - 1] == sys.maxsize:  # K번째 최단거리가 없으면 -1 출력
        print(-1)
    else:
        print(distance[i][K - 1])  # K번째 최단거리를 출력
