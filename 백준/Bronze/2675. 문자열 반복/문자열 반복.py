import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    ans = ""
    R, S = input().split()
    R = int(R)
    s = list(S)
    for i in range(len(s)):
        ans += s[i]*R
    print(ans)