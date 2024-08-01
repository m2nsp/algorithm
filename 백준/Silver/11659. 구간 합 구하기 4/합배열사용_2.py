N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0]                                      # 합을 저장할 배열
for i in range(1, N+1):
    S.append(S[i-1]+A[i-1])

for _ in range(M):
    j, k = map(int, input().split())
    ans = S[k]-S[j-1]
    print(ans)

# 인덱스 오류 조심하자!! 0부터 시작이니까!
