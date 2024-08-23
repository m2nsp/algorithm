import sys
from collections import deque
input = sys.stdin.readline

N = int(input())                                        # N : 도시의 수
M = int(input())                                        # M : 도로의 수

A = [[] for _ in range(N+1)]                            # A : 도로와 그 비용 저장
reverseA = [[] for _ in range(N+1)]                     # reverseA : 도착지를 기준으로 도로 저장
indegree = [0] * (N+1)                                  # indegree : 각 도시의 진입 차수 저장

# 그래프 입력 처리
for i in range(M):
    S, E, V = map(int, input().split())                 # S: 출발 도시, E: 도착 도시, V: 비용
    A[S].append((E, V))                           
    reverseA[E].append((S, V))
    indegree[E] += 1

startDosi, endDosi = map(int, input().split())          # 시작 도시, 도착 도시 입력받음

# 위상 정렬 및 최장 경로 계산
queue = deque()
queue.append(startDosi)
result = [0] * (N+1)

while queue:
    now = queue.popleft()
    for next in A[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now] + next[1])
        if indegree[next[0]] == 0:
            queue.append(next[0])

# 최장 경로를 이루는 간선 수 계산
resultCount = 0                                        # 최장 경로에 포함된 간선의 수 저장
visited = [False] * (N+1)
queue.clear()                                          # 큐 초기화
queue.append(endDosi)
visited[endDosi] = True

while queue:
    now = queue.popleft()
    for next in reverseA[now]:
        if result[next[0]] + next[1] == result[now]:
            resultCount += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])

print(result[endDosi])                                # 도착 도시까지의 최장 경로의 길이 출력
print(resultCount)                                    # 최장 경로를 구성하는 간선의 수 출력
