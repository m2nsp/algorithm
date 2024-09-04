import sys
input = sys.stdin.readline
N = int(input())    # 남은 일수
D = [0]*(N+2)    #  퇴사일까지 벌 수 있는 최대 수입 저장
T = [0]*(N+1)    # 상담에 필요한 일 수 저장
P = [0]*(N+1)    # 상담을 완료시 받는 수입 저장

for i in range(1, N+1):    # T, P 리스트 입력
    T[i], P[i] = map(int, input().split())
    
for i in range(N, 0, -1):
    if i+T[i] > N+1:    # i번째 상담을 퇴사일까지 끝낼 수 없을 때
        D[i] = D[i+1]
    else:    # i번째 상담을 퇴사일까지 끝낼 수 있을 때
        D[i] = max(D[i+1], P[i]+D[i+T[i]])
        
print(D[1])
