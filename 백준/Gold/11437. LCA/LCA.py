import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())     # N: 노드의 수
tree = [[] for _ in range(N+1)]    # 트리저장

# 트리 생성
for _ in range(0, N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
    
depth = [0]*(N+1)    # depth: 노드의 깊이 저장
parent = [0]*(N+1)    # parent: 노드의 조상 저장
visited = [False]*(N+1)    # visited: 방문 여부 저장 -- default:False

# BFS 함수
def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level = 1
    now_size = 1
    count = 0
    while queue:
        now_node = queue.popleft()
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now_node
                depth[next] = level
        count += 1
        if count == now_size:
            count = 0
            now_size = len(queue)
            level += 1
BFS(1)

# 빠른 LCA 함수
def executeLCA(a, b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp
    while depth[a] != depth[b]:
        a = parent[a]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

M = int(input())        # M: 질의 개수

for _ in range(M):
    a, b = map(int, input().split())
    print(str(executeLCA(a, b)))
    print("\n")
    
