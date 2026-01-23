from collections import deque, defaultdict

# 1. 입력받기
N, M, V = map(int, input().split())

# 2. 그래프 구현
graph = defaultdict(list)

for _ in range(M):
    k, e = map(int, input().split())
    graph[k].append(e)
    graph[e].append(k)
    
# 4. 번호가 작은 것부터 출력 -> 정렬
for v in range(1, N+1):
    graph[v].sort()

# 3. DFS
def dfs(graph, V):
    s = [V]
    visited = set([])
    
    while s:
        cur = s.pop()
        if cur in visited:
            continue
        visited.add(cur)
        print(cur, end=' ')
        
        for next in reversed(graph[cur]):  # 오름차순으로 출력 -> dfs는 스택이므로 반대로 넣기
            s.append(next)
    return None

# 4. BFS
def bfs(graph, V):
    q = deque([V])
    visited = set([V])
    
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        
        for next in graph[cur]:
            if next in visited:
                continue
            visited.add(next)
            q.append(next)
    return None
    
dfs(graph, V)
print()
bfs(graph, V)