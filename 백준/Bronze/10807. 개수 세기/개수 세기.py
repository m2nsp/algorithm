import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
V = int(input())

cnt = 0
for i in range(N):
    if A[i] == V:
        cnt += 1
print(cnt)
    