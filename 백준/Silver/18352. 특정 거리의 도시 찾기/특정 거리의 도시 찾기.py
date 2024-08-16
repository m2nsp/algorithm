import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())          # N: 도시 수, M: 도로 수, K: 거리 정보, X: 출발 도시
A = [[] for _ in range(N+1)]                    # 도로 정보를 저장할 리스트
ans = []                                        # K 거리만큼 떨어진 도시를 저장할 리스트
visited = [-1] * (N+1)                          # 방문 여부 및 거리를 저장할 리스트

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1                             # 출발 도시의 거리를 0으로 설정
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1:                # 아직 방문하지 않은 도시라면
                visited[i] = visited[now_Node] + 1  # 거리를 현재 도시의 거리 + 1로 설정
                queue.append(i)

for _ in range(M):                              # M개의 도로 정보 입력
    S, E = map(int, input().split())            # S -> E
    A[S].append(E)

bfs(X)  

for i in range(N+1):                            # 각 도시를 확인하여 K 거리만큼 떨어진 도시를 찾음
    if visited[i] == K:
        ans.append(i)

if not ans:                                     # K 거리만큼 떨어진 도시가 없으면 -1 출력, 있으면 도시 번호 출력
    print(-1)
else:
    ans.sort()  # 도시 번호를 오름차순으로 정렬
    for i in ans:
        print(i)
