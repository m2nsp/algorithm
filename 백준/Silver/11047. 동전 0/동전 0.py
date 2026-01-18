N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

sorted_coins = sorted(coins, reverse=True)

count = 0
for i in range(N):
    if sorted_coins[i] <= K:
        count += K//sorted_coins[i]
        K %= sorted_coins[i]
        
print(count)