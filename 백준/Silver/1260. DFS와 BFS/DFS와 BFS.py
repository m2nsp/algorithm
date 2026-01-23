from collections import deque
import sys
input = sys.stdin.readline
N, M , S = map(int, input().split())            # N:노드의 수/M:에지의 수/S:시작점
A = [[]for _ in range(N+1)]                     # 인접 리스트 생성

for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)                              # 인접 리스트 생성
    A[v].append(u)
    
for i in range(N+1):
    A[i].sort()                                 # 방문 가능한 노드가 여러 개일 경우 노드 번호가 작은 것을 방문
    
def dfs(v):                                     # dfs로 탐색 함수
    print(v, end=' ')
    visited[v]=True
    for i in A[v]:
        if not visited[i]:
            dfs(i)
        
visited = [False]*(N+1)                        # 방문기록 저장 리스트 초기화
dfs(S)

def bfs(v):                                    # bfs로 탐색 함수
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for i in A[current]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
print()
visited = [False]*(N+1)                        # 방문기록 저장 리스트 다시 초기화해야 됨
bfs(S)



# bfs는 주로 큐를 사용하여 구현함