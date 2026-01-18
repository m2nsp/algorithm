N = int(input())
P = list(map(int, input().split()))

S = [0]*N # 합배열
SP = sorted(P)

S[0] = SP[0]
for i in range(1, N):
    S[i] = S[i-1] + SP[i]

print(sum(S))