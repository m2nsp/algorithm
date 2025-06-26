import sys
input = sys.stdin.readline

A = []
for i in range(1, 10):
    k = int(input())
    A.append(k)
    
m = max(A)
for i in range(9):
    if A[i] == m:
        print(m)
        print(i+1)