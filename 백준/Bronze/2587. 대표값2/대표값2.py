N = []
for _ in range(5):
    N.append(int(input().strip()))

print(sum(N)//5)
N.sort()
print(N[2])