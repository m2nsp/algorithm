from collections import deque                                             # 파이썬에서는 큐를 deque로 구현***
N = int(input())                                                          # N = 카드의 개수
Q = deque()                                                               

for i in range(1, N+1):                                                   # 카드의 개수만큼 반복
    Q.append(i)                                                           # 큐에 카드 저장
while len(Q)>1:                                                           # 큐에 카드가 1장 남을 때까지 반복문 실행
    Q.popleft()                                                           # 맨위의 카드를 버림
    Q.append(Q.popleft())                                                 # 맨 위의 카드를 가장 아래 카드 밑으로 이동

print(Q[0])                                                               # 마지막으로 남은 카드 출력
