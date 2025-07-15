import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = [[]for _ in range(N+1)]
result = [0]*(N+1)

def dfs(start, parent):
    for neighbor in A[start]:
        if neighbor!= parent :
            result[neighbor] = start
            dfs(neighbor, start)
    

# 이중 연결 리스트 구현
for _ in range(N-1):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)
    
# 1을 루트노트로 했을때 탐색
dfs(1, 0)

# 결과 출력
#for i in range(2, N+1):
#    print(result[i])
print('\n'.join(map(str, result[2:])))