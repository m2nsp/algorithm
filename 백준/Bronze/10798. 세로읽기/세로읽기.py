A = [0]*5
m = 0    # 입력 중 가장 긴 길이
for i in range(5):
    A[i] = list(input())
    m = max(m, len(A[i]))

for j in range(m):
    for k in range(5):
        if j < len(A[k]):  # 인덱스가 존재할 때만 출력
            print(A[k][j], end='')