import sys
input = sys.stdin.readline
N, K = map(int, input().split())    # N: 총 개수, K: 선택 수
D = [[0 for i in range(N+1)] for i in range(N+1)]   # DP 테이블

for i in range(0, N+1):
    D[i][1] = i    # i개 중 1개를 뽑는 경우의 수는 i개
    D[i][0] = 1    # i개 중 1개도 선택하지 않는 경우의 수는 1개
    D[i][i] = 1    # i개 중 i개를 선택하는 경우의 수는 1개
    
for i in range(2, N+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]    # 조합 점화식
        
print(D[N][K])
