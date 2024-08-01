import heapq

N = int(input())
A = [0]*N
for i in range(N):
    A[i] = int(input())
min_heap = []

for i in range(N):
    heapq.heappush(min_heap, A[i])

# 힙에서 하나씩 꺼내어 출력
while min_heap:
    print(heapq.heappop(min_heap), end=' ')