N = int(input())                                                # 정점의 수
distance = [[0 for j in range(N)] for i in range(N)]            # 인접 행렬 초기화 - 경로의 존재 여부 저장

for i in range(N):                                              # 인접 행렬 입력
    distance[i] = list(map(int, input().split()))
        
for k in range(N):                                              # 플로이드-워셜 알고리즘 사용 -- 모든 쌍의 정점 간의 경로 확인
    for i in range(N):
        for j in range(N):
            if distance[i][k] == 1 and distance[k][j] == 1:     # i에서 k를 거쳐 j로 가는 경로가 존재한다면 i에서 j로 가는 경로도 존재함
                distance[i][j] = 1
                        
for i in range(N):                                              # 결과 출력
    for j in range(N):
        print(distance[i][j], end = ' ')
    print()
