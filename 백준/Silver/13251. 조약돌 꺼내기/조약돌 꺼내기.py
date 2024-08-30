D = [0] * 51
M = int(input())    # M: 색의 개수
D = list(map(int, input().split()))    #색깔별 조약돌 개수 저장
T = sum(D)    # T: 전체 조약돌 개수

K = int(input())    # K: 랜덤하게 뽑는 조약돌의 수
ans = 0    # 모두 같은 색일 확률 저장하는 변수

for i in range(M):
    if D[i] >= K:
        # i번째 그룹에서 K개를 선택할 확률을 계산
        prob = 1
        # K개의 아이템을 선택할 확률 계산
        for k in range(K):
            prob *= (D[i] - k) / (T - k)
        ans += prob

print(ans)
