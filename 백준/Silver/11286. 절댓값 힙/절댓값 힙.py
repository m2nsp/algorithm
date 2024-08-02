import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
Q = []

for _ in range(N):
    req = int(input())
    if req == 0:
        if len(Q) == 0:
            print('0\n')
        else:
            print(str(heapq.heappop(Q)[1]) + '\n')
    else:
        heapq.heappush(Q, (abs(req), req))
