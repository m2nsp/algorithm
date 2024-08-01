from collections import deque                              # deque 자료구조 사용
N, L = map(int, input().split())                           # 첫 번째 줄에서 N, L의 값을 읽어옴
D = deque()                                                # 슬라이딩 윈도우
current = list(map(int, input().split()))                  # 2번째 줄 입력값 읽어와서 리스트로 저장

for i in range(N):                                         # N 동안 반복 수행
    while D and D[-1][1] > current[i]:                     # 현재 값보다 값이 큰 경우 pop수행
        D.pop()
    D.append((i, current[i]))                              # 현재 값을 덱에 저장
    if D[0][0] <= i-L:                                     # 슬라이딩 윈도우의 범위 초과할 경우
        D.popleft()                                        # 덱에서 제거
    print(D[0][1], end=' ')                                # 남아 있는 값이 최솟값