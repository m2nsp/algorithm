import sys
input = sys.stdin.readline
D = [[0 for j in range(15)] for i in range(15)]        # DP 테이블 생성

# DP테이블 초기화
for i in range(1, 15):
    D[i][1] = 1
    D[0][i] = i
    
for i in range(1, 15):
    for j in range(2, 15):
        D[i][j] = D[i][j-1] + D[i-1][j]        # 조합 점화식
        
T = int(input())    # T: 질의의 수


# 질의 구하기
for i in range(0, T):
    K = int(input())    # K:층 N:호
    N = int(input())
    print(D[K][N])
