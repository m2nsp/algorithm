import heapq

N, L = map(int, input().split())                        # 첫 번째 줄
current = list(map(int, input().split()))               # 두 번째 줄 
M = []                                                  # 각 윈도우에서의 최소값을 저장하는 리스트
min_heap = []                                           # 현재 슬라이딩 윈도우 내의 요소들을 저장하는 최소 힙

for i in range(N):
    heapq.heappush(min_heap, (current[i], i))           # 현재 값 최소힙에 저장
    # 윈도우 범위 밖의 요소 제거
    while min_heap[0][1] <= i - L:                      # 최소 값이 슬라이딩 윈도우의 범위 내에 있는 지 확인
        heapq.heappop(min_heap)                         # 범위 밖에 있을 경우 제거
                                                                        # 이때 최소 값이 아닌 값들은 남아있어도 상관 없기 때문에 굳이 검사하지 않음
    M.append(min_heap[0][0])                            # 최소 힙에서 최소값은 항상 힙의 루트에 위치하므로, min_heap[0][0]를 M 리스트에 추가

print(" ".join(map(str, M)))                            # 결과 값 출력
