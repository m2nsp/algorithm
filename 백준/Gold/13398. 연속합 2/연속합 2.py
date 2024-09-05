N = int(input())    # N: 수열의 크기
A = list(map(int, input().split()))    # A: 수열 데이터 저장하는 리스트

# index 포함 최대 연속 합 구하기 
L = [0]*N
L[0] = A[0]
result = L[0]

for i in range(1, N):
    L[i] = max(A[i], L[i-1]+A[i])
    result = max(result, L[i])    # 제거하지 않았을 때는 기본 최댓값으로 저장
    
R = [0]*N
R[N-1] = A[N-1]

for i in range(N-2, -1, -1):
    R[i] = max(A[i], R[i+1]+A[i])
    
for i in range(1, N-1):
    temp = L[i-1]+R[i+1]
    result = max(result, temp)
    
print(result)
