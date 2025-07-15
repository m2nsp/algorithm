import sys
input = sys.stdin.readline
import heapq

N = int(input())

min_heap = []
# 최소 힙 만들기
for _ in range(N):
    heapq.heappush(min_heap, int(input()))
# 누적 합 최소힙에 넣는 것 반복
total = 0
while len(min_heap) > 1:
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)
    total += (a+b)
    heapq.heappush(min_heap, a+b)
print(total)
    