import sys
import heapq

input = sys.stdin.readline

# N: 노드 수, M: 간선 수, K: K번째 최단 경로를 찾기 위한 수
N, M, K = map(int, input().split())

# 그래프 초기화
W = [[] for _ in range(N + 1)]
# 각 노드에서 K번째로 작은 최단거리를 저장할 리스트를 초기화
# distance[i][j]는 노드 i까지 가는 j번째로 작은 거리
distance = [[sys.maxsize] * K for _ in range(N + 1)]

# 간선 정보를 입력받음
for _ in range(M):
    a, b, c = map(int, input().split())
    W[a].append((b, c))  # 노드 a에서 b로 가는 비용이 c인 간선

# 우선순위 큐 초기화, (비용, 노드)
pq = [(0, 1)]
# 시작 노드 (1번 노드)의 첫 번째 최단거리를 0으로 초기화
distance[1][0] = 0

# 다익스트라 알고리즘 변형을 사용하여 K번째 최단거리를 계산
while pq:
    cost, node = heapq.heappop(pq)  # 현재 노드와 누적 비용을 꺼냄
    for nNode, nCost in W[node]:  # 현재 노드와 연결된 다른 노드들 확인
        sCost = cost + nCost  # 새로운 누적 비용 계산
        # 새롭게 계산한 누적 비용이 해당 노드의 K번째 최단거리보다 작으면 업데이트
        if distance[nNode][K - 1] > sCost:
            distance[nNode][K - 1] = sCost  # K번째 최단거리를 업데이트
            distance[nNode].sort()  # K개의 최단거리를 정렬하여 K번째가 가장 큰 값이 되도록 유지
            heapq.heappush(pq, [sCost, nNode])  # 우선순위 큐에 새로운 경로를 추가

# 모든 노드에 대해 K번째 최단거리를 출력
for i in range(1, N + 1):
    if distance[i][K - 1] == sys.maxsize:  # K번째 최단거리가 없으면 -1 출력
        print(-1)
    else:
        print(distance[i][K - 1])  # K번째 최단거리를 출력
