import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    if A[i] < X:
        ans.append(A[i])

for j in ans:
    print(j, end=" ")