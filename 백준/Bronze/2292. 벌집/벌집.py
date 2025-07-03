import sys
input = sys.stdin.readline
N = int(input().strip())

n = N-1
i = 1
while True:
    if n <= 0:
        ans = i
        break
    n = n-(i*6)
    i += 1
print(ans)