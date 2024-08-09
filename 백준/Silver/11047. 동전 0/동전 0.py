N, K = map(int, input().split())               # N: 동전의 종류, K: 목표 금액
A = [0] * N

for i in range(N):
    A[i] = int(input())                        # 주어진 동전의 가격 저장
    
cnt = 0                                        # 동전의 개수 최솟값 저장하는 변수 초기화

for i in range(N-1, -1, -1):                   # 가격이 큰 동전에서부터 작은 동전으로 가면서 계산
    if A[i] <= K:                              # 남은 금액보다 동전의 가격이 같거나 작아야 사용 가능
        cnt += K // A[i]                       # 사용한 동전의 개수 더하기
        K = K % A[i]                           # 남은 금액 갱신

print(cnt)                                     # 최소 동전 개수 출력
