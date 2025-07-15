import sys
import heapq
input = sys.stdin.readline

max_heap=[]
N = int(input())
for _ in range(N):
    c = int(input())
    if c==0:
        if not max_heap:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, -c)