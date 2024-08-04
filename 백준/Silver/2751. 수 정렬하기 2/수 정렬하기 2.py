N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))

sorted_A = sorted(A)

for i in range(N):
    print(sorted_A[i])