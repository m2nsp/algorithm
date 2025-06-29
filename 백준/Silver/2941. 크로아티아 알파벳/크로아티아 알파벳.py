import sys
input = sys.stdin.readline

S = list(input().strip())
cnt = 0
i = 0

while i < len(S):
    if i+2 < len(S) and S[i] == 'd' and S[i+1] == 'z' and S[i+2] == '=':
        cnt += 1
        i += 3
    elif i+1 < len(S) and S[i] + S[i+1] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

print(cnt)
