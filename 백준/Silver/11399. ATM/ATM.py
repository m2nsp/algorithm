N = int(input())
A = list(map(int, input().split()))

S = []
for i in range(N):
    S.append((i, A[i]))

# A[i]를 기준으로 정렬
S_sorted = sorted(S, key=lambda x: x[1])

ans = [0]*N
for i in range(N):
    if i==0:
        ans[i] = S_sorted[i][1]
    else:
        ans[i] += S_sorted[i][1] + ans[i-1]

Ans = 0
for i in range(N):
    Ans += ans[i]

print(Ans)