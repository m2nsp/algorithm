import sys
input = sys.stdin.readline

cnt = 0
N = int(input().strip())
for _ in range(N):
    ans = True
    S = list(input().strip())
    for i in range(1, len(S)):
        if S[i] != S[i-1] and S[i] in S[:i]:
            ans = False
    if ans == True:
        cnt += 1
    
print(cnt)