# 종료 시간이 빠를수록 다음 회의와 겹치지 않게 시작하는데 유리함

N = int(input())                            # N : 회의 수
A = [[0]*2 for _ in range(N)]               # A : 주어진 회의들 저장할 배열

for i in range(N):
    u, v = map(int, input().split())        # 시작, 종료시간을 각각 받아옴
    A[i][0] = v
    A[i][1] = u
    
A.sort()                                    # 종료 시간이 빠른 순으로 정렬됨  -- 종료 시간을 0번 인덱스에 미리 저장함 -- sort()함수는 기본적으로 0번 인덱스를 기준으로 정렬을 수행함
cnt = 0                                     # 진행할 수 있는 회의의 수 저장하는 변수
end = -1                                    # 종료 시각 나타내는 변수

for i in range(N):
    if A[i][1] >= end:                      # 겹치지 않는 회의 등장
        end = A[i][0]                        
        cnt += 1 
        
print(cnt)
