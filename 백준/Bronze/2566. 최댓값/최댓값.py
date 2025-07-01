import sys
input = sys.stdin.readline

A = [[0 for _ in range(9)] for _ in range(9)]
k = 0
k_col = 0
k_row = 0
for i in range(9):
    A[i] = list(map(int, input().split()))
    q = max(A[i])
    if k < q:
        k = q
        k_col = A[i].index(q)
        k_row = i
print(k)
print(k_row+1, k_col+1)
    