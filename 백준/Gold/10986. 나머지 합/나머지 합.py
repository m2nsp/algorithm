# 특정 구간 수들의 나머지 연산을 더해 나머지 연산을 한 값과 이 구간 합의 나머지 연산을 한 값은 동일하다

import sys
input = sys.stdin.readline                          # 입력

n, m = map(int, input().split())                    # 주어진 수 받기: n: 수열의 개수/ m: 나누어 떨어져야하는 수
A = list(map(int, input().split()))                 # A : 주어진 수들 저장

S = [0]*n                                           # 합배열
C = [0]*m                                           # 나머지가 i인 수들의 개수 저장
S[0] = A[0]                                         # 합배열 초기화
ans = 0                                             # 정답

for i in range(1, n):
    S[i] = S[i-1]+A[i]                              # 합 저장

for i in range(n):
    remainder = S[i] % m                            # 합의 나머지 구하기
    if remainder == 0:                              # 그 결과가 0인 경우 정답에 더하기
        ans += 1
    C[remainder] += 1                               # 아니면 나머지가 i 이면 C[i]에 더하기

for i in range(m):
    if(C[i] > 1):                   
        ans += (C[i]*(C[i]-1) //2)                  # 나머지가 같은 인덱스 중 2개 뽑는 경우 더하기
        
print(ans)


# 이 문제 복습 필요