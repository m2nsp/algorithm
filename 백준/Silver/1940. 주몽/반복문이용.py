N = int(input())                        # 재료의 수
M = int(input())                        # 갑옷의 번호
A = list(map(int, input().split()))     # 주어진 재료들의 번호
count = 0                               # 만들 수 있는 갑옷의 수
for i in range(N):
    for j in range(N):
        if A[i]+A[j] == M:              # 두 재료 번호의 합이 M인 경우
            count += 1                  # count 증가시킴

print(count//2)                         # A[i] + A[j] 와 A[j] + A[i]는 같은 경우이므로 2로 나눠줌
