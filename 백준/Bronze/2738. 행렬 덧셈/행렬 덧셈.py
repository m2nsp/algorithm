import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)]
B = [[0 for _ in range(M)] for _ in range(N)]
C = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))
for i in range(N):
    B[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
    
for i in range(N):
    for j in range(M):
        print(C[i][j], end=" ")
    print()