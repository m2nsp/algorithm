import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0]*N

for i in range(M):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        A[l-1] = k
        
for num in A:
    print(num, end=" ")