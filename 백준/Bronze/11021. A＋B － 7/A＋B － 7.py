import sys
input = sys.stdin.readline

T = int(input())
for k in range(1, T+1):
    i, j = map(int, input().split())
    sum = i+j
    print(f"Case #{k}: {i+j}")