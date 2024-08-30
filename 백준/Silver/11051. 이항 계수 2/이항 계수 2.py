import sys
input = sys.stdin.readline
N, K = map(int, input().split())    # 이항계수 (N K) 구하기
D = [[0 for j in range(N+1)] for i in range(N+1)]    # DP 테이블

# DP 테이블 초기화
for i in range(0, N+1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1
    
for i in range(2, N+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]    # 조합 점화식
        D[i][j] = D[i][j] % 10007
        
print(D[N][K])