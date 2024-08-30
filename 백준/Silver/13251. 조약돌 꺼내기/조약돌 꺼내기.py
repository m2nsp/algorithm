D = [0] * 51
M = int(input())
D = list(map(int, input().split()))
T = sum(D)

K = int(input())
ans = 0

for i in range(M):
    if D[i] >= K:
        # i번째 그룹에서 K개를 선택할 확률을 계산
        prob = 1
        for k in range(K):
            prob *= (D[i] - k) / (T - k)
        ans += prob

print(ans)
