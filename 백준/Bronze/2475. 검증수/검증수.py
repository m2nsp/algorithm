nums = input().split()
s = 0
for n in nums:
    n = int(n)
    s += (n**2)
ans = s % 10
print(ans)