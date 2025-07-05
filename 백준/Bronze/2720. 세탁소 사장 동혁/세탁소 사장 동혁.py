import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    C = int(input())
    cnt_q = C//25
    C = C % 25
    cnt_d = C//10
    C = C % 10
    cnt_n = C//5
    C = C % 5
    cnt_p = C
    print(cnt_q, cnt_d, cnt_n, cnt_p)