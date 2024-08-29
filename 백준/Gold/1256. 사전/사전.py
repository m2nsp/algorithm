import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())                    # N: a 문자 개수, M: z 문자 개수, K: 순번
D = [[0 for j in range(202)] for i in range(202)]      # D: 조합 경우의 수 저장 테이블

# 조합 값을 미리 계산하여 D에 저장
for i in range(0, 201):            # i : 전체 문자 개수
    for j in range(0, i+1):    # j는 'z'의 개수
        if j == 0 or j == i:
            D[i][j] = 1
        else:
            D[i][j] = D[i-1][j-1] + D[i-1][j]    # 조합 점화식
            if D[i][j] > 1000000000:    # D[i][j]의 값이 K의 범위를 넘어간 경우
                D[i][j] = 1000000001

if D[N+M][M] < K:    # 규완이의 사전에 수록돼 있는 문자열의 개수가 K보다 작은 경우
    print(-1)
else:    # 사전 순으로 K번째 문자열을 구하는 경우
    while not (N == 0 and M == 0):    # 모든 a와 z를 사용해 문자열을 완성할 때까지 반복
        if N > 0 and D[N-1+M][M] >= K:    # 만약 a로 시작하는 경우의 수가 K보다 크거나 같다면
            print("a", end='')
            N -= 1
        else:
            print("z", end='')
            if N > 0:
                K -= D[N-1+M][M] 
            M -= 1

"""
조합을 구할 때 a+b=d 인 경우, dCa = dCb 이므로 여기서는 a의 위치를 조합으로 배치하는 경우를 생각하면 아닌 자리에 자동으로 z가 들어가면 됨
"""
