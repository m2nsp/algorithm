import sys
input = sys.stdin.readline

M, N = map(int, input().split())            # M이상 N이하

A = [1]*(N+1)                               # 배열 초기화
A[0] = A[1] = 0                             # 0과 1은 소수가 될 수 없으므로 미리 0으로 설정

for i in range(2, N+1):                     # M이상 N이하
    for j in range(i+i, N+1, i):
        A[j] = 0                            # i의 배수 소수에서 제외
        
for i in range(M):                          # M 미만의 수 제외
    A[i] = 0

for i in range(N+1):
    if(A[i] == 1):                          # A의 값이 1인 경우 i가 소수임
        print(i)
