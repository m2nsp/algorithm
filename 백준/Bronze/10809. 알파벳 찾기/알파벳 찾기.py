import sys
input = sys.stdin.readline

A = list(input().strip())
for i in range(26):
    idx = chr(ord('a') + i)
    try:
        ans = A.index(idx)    # i번째 알파벳의 인덱스
        print(ans, end=" ")
    except:
        print(-1, end=" ")