# 종료 시간이 빠를수록 다음 회의와 겹치지 않게 시작하는데 유리함

N = int(input())                            # N : 회의 수
A = [[0]*2 for _ in range(N)]               # A : 주어진 회의들 저장할 배열

for i in range(N):
    u, v = map(int, input().split())
    A[i][0] = v
    A[i][1] = u
    
A.sort()                                    # 종료 시간이 빠른 순으로 정렬됨
cnt = 0
end = -1                                    # 종료 시각 나타내는 변수

for i in range(N):
    if A[i][1] >= end:                      # 겹치지 않는 회의 등장
        end = A[i][0]                        
        cnt += 1 
        
print(cnt)
