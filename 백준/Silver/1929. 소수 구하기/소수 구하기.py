import sys
input = sys.stdin.readline

M, N = map(int, input().split())

A = [1]*(N+1)
A[0] = A[1] = 0

for i in range(2, N+1):         # M이상 N이하
    for j in range(i+i, N+1, i):
        A[j] = 0
        
for i in range(M):
    A[i] = 0

for i in range(N+1):
    if(A[i] == 1):
        print(i)