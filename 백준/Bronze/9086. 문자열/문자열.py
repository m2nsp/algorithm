import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    case = list(input().strip())
    st = case[0]
    end = case[-1]
    ans = st + end
    print(ans)