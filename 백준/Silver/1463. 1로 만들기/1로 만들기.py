import sys
input = sys.stdin.readline
N = int(input())    # 구하고자 하는 수
D = [0]*(N+1)
D[1] = 0    # 1일때는 연산 필요없음

for i in range(2, N+1):
    D[i] = D[i-1]+1   
    if i%2 == 0:
        D[i] = min(D[i], D[i//2]+1)    # 나누기 2연산
    if i%3==0:
        D[i] = min(D[i], D[i//3]+1)    # 나누기 3연산
print(D[N])
