import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(set(A))

rank = { value: idx for idx, value in enumerate(sorted_A)}

C = [rank[x] for x in A]
print(*C)