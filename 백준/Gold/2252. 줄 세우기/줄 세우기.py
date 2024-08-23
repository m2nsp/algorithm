from collections import deque
N, M = map(int, input().split())                        # N: 노드 개수 , M: 간선 개수 
A = [[]for _ in range(N+1)]                             # A: 각 노드에 연결된 노드들 저장 리스트
indegree = [0]*(N+1)                                    # 각 노드의 진입 차수 저장

for i in range(M):                                      # 간선 정보 저장
    S, E = map(int, input().split())
    A[S].append(E)
    indegree[E]+=1
queue=deque()                                           # 큐 생성

for i in range(1, N+1):
    if indegree[i]==0:                                  # 진입 차수가 0인 노드 큐에 삽입
        queue.append(i)
        
while queue:                                            # 위상 정렬 수행
    now = queue.popleft()
    print(now, end=' ')
    for next in A[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
            
