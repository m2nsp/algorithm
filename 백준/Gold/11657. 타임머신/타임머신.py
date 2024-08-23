import sys
input = sys.stdin.readline
N, M = map(int, input().split())                            # N : 도시의 수 , M : 버스 노선의 수
edges = []                                                  # 간선 리스트
distance = [sys.maxsize]*(N+1)                              # 최단 거리 리스트

for i in range(M):                                          # 간선 정보 입력
    start, end, time = map(int, input().split())            # start: 시작 도시, end: 도착 도시, time: 걸리는 시간
    edges.append((start, end, time))
    
distance[1] = 0                                             # 시작 도시의 최단거리 = 0

for _ in range(N-1):                                        # 벨만-포드 알고리즘 
    for start, end, time in edges: 
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time          # 도시의 거리가 초기값 아니고, 현재 간선을 거쳐 가는 것이 더 빠르면 갱신
            
mCycle = False                                              # 음수 사이클 여부 저장하는 변수

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True
        break                                               # 음수 사이클 존재 시 더 이상 확인할 필요 없음
        
if not mCycle:                                              # 음수 사이클 존재 안 할 경우 = 최단 거리 출력
    for i in range(2, N+1):
        if distance[i]!=sys.maxsize:
            print(distance[i])
        else:                                               # 도달할 수 없는 도시
            print(-1)
else:                                                       # 음수 사이클이 존재하는 경우                                     
    print(-1)
