import sys
input = sys.stdin.readline
N = int(input())                                # N : 도시의 수
M = int(input())                                # M : 버스 노선의 수
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]        # 최단 거리 배열 초기화

for i in range(1, N+1):                         # 자기 자신으로 가는 거리 = 0
    distance[i][i] = 0
    
for i in range(M):                              # 간선 정보 입력
    s, e, v = map(int, input().split())         # s: 출발 도시, e: 도착 도시, v: 비용
    if distance[s][e] > v:
        distance[s][e] = v
        
for k in range(1, N+1):                        # 플로이드-워셜 알고리즘 이용하여 모든 쌍의 최단 거리 계산
    for i in range(1, N+1):                    # 중간 경유 도시 k, 출발 도시 i, 도착 도시 j
        for j in range(1, N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:     # i에서 j로 가는 최단 거리가 k를 거쳐서 가는 것보다 크다면 업데이트
                distance[i][j] = distance[i][k] + distance[k][j]
                
for i in range(1, N+1):                        # 결과 출력
    for j in range(1, N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')                  # i에서 j로 갈 수 없는 경우 = 0
        else:
            print(distance[i][j], end=' ')
    print()
