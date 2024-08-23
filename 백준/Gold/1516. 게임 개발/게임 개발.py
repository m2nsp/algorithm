from collections import deque

N = int(input())                                            # N : 건물 수
A = [[] for _ in range(N+1)]                                # A : 건물의 선행 건물 저장
indegree = [0]*(N+1)                                        # 진입 차수 저장
selfBuild = [0]*(N+1)                                       # 짓는 데 걸리는 시간 저장

for i in range(1, N+1):                                     # 건물별 건설 시간 및 선행 작업 입력
    inputList = list(map(int, input().split()))
    selfBuild[i] = inputList[0]                             # 건물 i의 건설 시간
    index = 1
    while True:
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:                                   
            break
        A[preTemp].append(i)                               # 선행 건물이 완료된 후에야 건물 i 건설 가능
        indegree[i] += 1                                   # 건물 i의 진입 차수 증가
        
queue = deque()                                            # 위상정렬 -- 큐 생성 

for i in range(1, N+1):                                    # 진입 차수가 0인 건물 삽입
    if indegree[i] == 0:
        queue.append(i)
        
result = [0]*(N+1)                                         # 각 건물을 완성하는 데 걸리는 최종 시간 저장

while queue:                                               # 위상 정렬 알고리즘 수행
    now = queue.popleft()
    for next in A[now]:  
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + selfBuild[now])
        if indegree[next] == 0: 
            queue.append(next)
            
for i in range(1, N+1):                                    # 결과 출력
    print(result[i] + selfBuild[i])
