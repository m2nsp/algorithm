import sys
input = sys.stdin.readline
N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))

count = 0
changed = False

for i in range(N):
    changed = False
    for j in range(N-i-1):
        if A[j] > A[j+1]:
           A[j], A[j+1] = A[j+1], A[j]
           changed = True
    if not changed:
        count = i + 1
        break

sys.stdout.write(str(count) + '\n')
