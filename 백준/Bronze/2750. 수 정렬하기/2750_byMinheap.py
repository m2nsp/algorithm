import heapq

N = int(input())                    # 첫번째 줄 수의 개수 읽어옴
A = [0]*N                           # 주어진 N개의 숫자 저장하는 리스트
for i in range(N):
    A[i] = int(input())             # 주어진 수 저장하기
min_heap = []                       # 최소 힙

for i in range(N):
    heapq.heappush(min_heap, A[i])      # 힙에 수 저장하기

# 힙에서 하나씩 꺼내어 출력
while min_heap:
    print(heapq.heappop(min_heap), end=' ')
