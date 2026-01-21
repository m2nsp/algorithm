T = int(input())
cases = [input() for _ in range(T)]
cnt = 0
ans = 0
for i in range(len(cases)):
    for s in list(cases[i]):
        if s == 'X':
            cnt = 0
        elif s == 'O':
            cnt += 1
            ans += cnt
    print(ans)
    cnt = 0
    ans = 0