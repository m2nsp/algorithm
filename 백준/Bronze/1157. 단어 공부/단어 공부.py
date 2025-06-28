import sys
input = sys.stdin.readline

S = input().strip()
S = S.upper()
A = list(set(S))

cnt_A = [0]*len(A)
for i in range(len(A)):
    cnt_A[i] = S.count(A[i])


max_idx = cnt_A.index(max(cnt_A))     #최댓값의 인덱스
max_val = max(cnt_A)                  #최댓값의 값

dup = 0
for i in range(len(A)):
    if cnt_A[i] == max_val:
        dup += 1
if dup >= 2:
    print('?')
else:
    print(A[max_idx])