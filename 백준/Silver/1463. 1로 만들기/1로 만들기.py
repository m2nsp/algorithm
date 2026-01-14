def min_operations_to_one(N):
  dp = [0] * (N+1)
  dp[1] = 0
  
  for i in range(1, N+1):
    if i > 1:
        dp[i] = dp[i-1]+1
        if i >= 2 and i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i >= 3 and i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
  return dp[i]

n = int(input())
ans = min_operations_to_one(n)
print(ans)