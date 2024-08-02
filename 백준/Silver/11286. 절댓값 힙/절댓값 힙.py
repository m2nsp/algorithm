import heapq
import sys
input = sys.stdin.readline                                            # 실행시간 최적화 하기 위한 부분
print = sys.stdout.write

N = int(input())                                                      # N : 연산의 개수
Q = []                                                                # 우선순위 큐 리스트로 구현

for _ in range(N):                                                    
    req = int(input())                                                # 입력 값 받아옴
    if req == 0:                        
        if len(Q) == 0:                                               # Q.empty()대신 len(Q) 사용 - Q.empty()는 보통 PriorityQueue 환경에서 사용
            print('0\n')                                              # 큐가 비어있음 
        else:
            print(str(heapq.heappop(Q)[1]) + '\n')                    # 큐에서 최솟값 꺼내어 출력
    else:
        heapq.heappush(Q, (abs(req), req))                            # 절댓값을 기준으로 우선순위 결정

"""
단일 스레드에서는 PriorityQueue 보다 heapq 가 더 가볍고 빠름
heapq 는 리스트를 힙처럼 다루는 것임
"""
