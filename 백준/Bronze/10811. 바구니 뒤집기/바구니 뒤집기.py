import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [i for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    A[a:b+1] = A[a:b+1][::-1]
    
#print(A[1::])
for i in range(1, N+1):
    print(A[i], end=" ")    