import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [0]*(N+1)
for i in range(1, N+1):
    A[i] = i

for _ in range(M):
    i, j = map(int, input().split())
    A[i], A[j] = A[j], A[i]
    
for i in range(1, N+1):
    print(A[i], end=" ")