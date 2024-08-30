import sys
input = sys.stdin.readline
D = [[0 for j in range(31)] for i in range(31)]

# DP 테이블
for i in range(0, 31):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1
    
for i in range(2, 31):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]
        
t = int(input())    # t: 질의의 수

# 질의 처리
for i in range(0, t):
    N, M = map(int, input().split())
    print(D[M][N])
