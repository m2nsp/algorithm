paper = [[0]*100 for _ in range(100)]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)