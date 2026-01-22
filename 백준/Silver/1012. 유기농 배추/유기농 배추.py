di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(matrix, M, N, x, y):
    s = [(x, y)]
    visited[x][y] = True
    
    while s:
        ci, cj = s.pop()
        
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            
            if not (0<=ni and ni < N and 0 <= nj and nj < M):
                continue
            if matrix[ni][nj] == 0:
                continue
            if visited[ni][nj]:
                continue
                
            visited[ni][nj] = True
            s.append((ni, nj))
    return None

def worms_cnt(N, M, matrix, visited):
    cnt = 0
    for p in range(N):
        for q in range(M):
            if visited[p][q] or matrix[p][q] == 0:
                continue
            else:
                dfs(matrix, M, N, p, q)
                cnt += 1
    return cnt

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    
    matrix = [[0]* (M) for _ in range(N)]
    visited = [[False]* M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        
    print(worms_cnt(N, M, matrix, visited))
