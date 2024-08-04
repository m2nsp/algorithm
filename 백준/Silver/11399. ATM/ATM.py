N = int(input())                                                    # N : 사람 수
A = list(map(int, input().split()))                                 # 각 사람의 주어진 인출 시간

S = []                                                              # 인덱스와 인출시간 동시에 저장하는 배열
for i in range(N):
    S.append((i, A[i]))

# A[i]를 기준으로 정렬
S_sorted = sorted(S, key=lambda x: x[1])

ans = [0]*N                                                        # 각 사람의 총 걸리는 시간을 계산해서 저장하는 합 배열
for i in range(N):
    if i==0:
        ans[i] = S_sorted[i][1]
    else:
        ans[i] += S_sorted[i][1] + ans[i-1]

Ans = 0                                                             # 총 인출시간을 저장하는 변수
for i in range(N):
    Ans += ans[i]

print(Ans)
