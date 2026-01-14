N = int(input())
dp = [0] + [5000] * N

def deliver(n):
    for i in range(1, N+1):
        if i >= 3:
            dp[i] = min(dp[i-3]+1, dp[i-5]+1)
    return dp[i]
ans = deliver(N)

if ans >= 5000:
    print(-1)
else:
    print(ans)