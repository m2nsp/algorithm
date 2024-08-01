N = int(input())
A = [0]*N
for i in range(N):
    A[i] = int(input())

A.sort()

for item in A:
    print(item, end=' ')