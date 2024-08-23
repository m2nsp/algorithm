N = int(input())                                                # N : 도시의 수
M = int(input())                                                # M : 여행계획에 포함된 도시의 수
D = [[0 for j in range(N+1)] for i in range(N+1)]               # D : 도시간의 인접행렬

def find(a):                                                    # 특정 노드의 루트를 찾는 함수
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b):                                                # 두 노드를 같은 집합으로 합치는 함수
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
for i in range(1, N+1):                                         # 도시간의 연결 정보 저장
    D[i] = list(map(int, input().split()))
    D[i].insert(0, 0)
    
route = list(map(int, input().split()))                        # 여행 계획에 포함된 도시들 저장
route.insert(0, 0)
    
parent = [0]*(N+1)                                             # 각 노드의 부모 노드 저장

for i in range(1, N+1):
    parent[i] = i                                              # 처음에는 자기자신 저장
    
for i in range(1, N+1):                                        # 유니온 연산 수행
    for j in range(1, N+1):
        if D[i][j] == 1:
            union(i, j)
            
index = find(route[1])                                        # 여행 계획이 같은 집합에 속하는 지 확인
isConnect = True
for i in range(2, len(route)):
    if index != find(route[i]):
        isConnect = False
        break
        
if isConnect:                                                # 같은 집합에 속하면: YES, 아니면: NO
    print("YES")
else:
    print("NO")
