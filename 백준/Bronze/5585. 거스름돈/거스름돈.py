N = int(input())
coins = [500, 100, 50, 10, 5, 1]
def min_change(n):
    rest = n
    count = 0
    while rest > 0:
        for coin in coins:
            if rest >= coin:
                rest -= coin
                count += 1
                break
    return count

print(min_change(1000-N))