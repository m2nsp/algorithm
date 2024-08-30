import sys
input = sys.stdin.readline

# 팩토리얼 값을 저장할 배열
F = [0] * 21
S = [0] * 21
visited = [False] * 21

# 숫자 N을 입력받습니다.
N = int(input())
F[0] = 1

# 팩토리얼 계산
for i in range(1, N + 1):
    F[i] = F[i - 1] * i
    
# 입력 리스트를 받아옵니다.
inputList = list(map(int, input().split()))

# 첫 번째 경우: k번째 순열을 찾아야 하는 경우
if inputList[0] == 1:
    K = inputList[1]
    
    # 순열을 구성하기 위한 루프
    for i in range(1, N + 1):
        cnt = 1
        for j in range(1, N + 1):
            if visited[j]:
                continue
            if K <= cnt * F[N - i]:
                K -= (cnt - 1) * F[N - i]
                S[i] = j
                visited[j] = True
                break
            cnt += 1
    
    # 결과 출력
    for i in range(1, N + 1):
        print(S[i], end=' ')

# 두 번째 경우: 주어진 순열이 몇 번째 순열인지 찾아야 하는 경우
else:
    K = 1
    for i in range(1, N + 1):
        cnt = 0
        for j in range(1, inputList[i]):
            if not visited[j]:
                cnt += 1
        K += cnt * F[N - i]
        visited[inputList[i]] = True
    
    # 결과 출력
    print(K)
