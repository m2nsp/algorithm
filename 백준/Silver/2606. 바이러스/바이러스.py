from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
E = int(input())

graph = defaultdict(list)
visited = set()
cnt = 0

for _ in range(E):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

def dfs(cur):    
    visited.add(cur)
    cnt = 1
    
    for next in graph[cur]:
        if next not in visited:
            cnt += dfs(next)
    return cnt
            
print(dfs(1)-1)