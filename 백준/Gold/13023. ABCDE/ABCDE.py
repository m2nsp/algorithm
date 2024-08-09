import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())        # N : 캠프 참가 인원, M : 친구 관계의 수
arrive = False                          # 도착 했는지 확인하는 변수 초기화
A = [[]for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[now] = False
    
for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)
    
for i in range(N):
    dfs(i, 1)
    if arrive:
        break
 
if arrive:
    print(1)
else:
    print(0)