import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

# 입력받기
N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
    
depth = [0] * (N+1)
visited = [False] * (N+1)
temp = 1
kmax = 0

# kmax 구하기
while temp <= N:
    temp <<= 1
    kmax += 1
    
parent = [[0] * (N+1) for _ in range(kmax+1)]

# BFS를 이용하여 depth 및 parent[0] 설정
def BFS(node):
    queue = deque([node])
    visited[node] = True
    level = 1
    while queue:
        for _ in range(len(queue)):
            now_node = queue.popleft()
            for next_node in tree[now_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    parent[0][next_node] = now_node
                    depth[next_node] = level
        level += 1

BFS(1)

# 2^k 부모 설정
for k in range(1, kmax+1):
    for n in range(1, N+1):
        parent[k][n] = parent[k-1][parent[k-1][n]]

# LCA 함수 구현
def executeLCA(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    
    # b를 a의 깊이까지 올리기
    for k in range(kmax, -1, -1):
        if depth[b] - depth[a] >= (1 << k):
            b = parent[k][b]
    
    if a == b:
        return a
    
    # LCA 찾기
    for k in range(kmax, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    
    return parent[0][a]

# 질의 처리
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    lca = executeLCA(a, b)
    print(str(lca) + "\n")
