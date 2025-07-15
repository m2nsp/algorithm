import heapq
import sys
input = sys.stdin.readline

N = int(input()) #연산 개수

ar = []
for _ in range(N):
    c = int(input())
    if c==0 and not ar:
        print(0)
    elif c==0:
        m = heapq.heappop(ar)
        print(m)
    else:
        heapq.heappush(ar, c)