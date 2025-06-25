import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    i, j = map(int, input().split())
    print(i+j)
    