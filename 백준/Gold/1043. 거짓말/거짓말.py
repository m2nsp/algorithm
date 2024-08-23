N, M = map(int, input().split())                            # N: 사람의 수, M: 파티의 수 
trueP = list(map(int, input().split()))                     # 진실 알고 있는 사람들
T = trueP[0]                                                # trueP의 수
del trueP[0]                                                # 첫번째 요소는 필요 없음
result = 0                                                  # 거짓말 할 수 있는 파티의 수 저장
party = [[] for _ in range(M)]                              # 각 파티에 참석한 사람들 저장

def find(a):                                                # 부모를 찾는 함수
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b):                                            # 유니온 함수 -- 같은 그룹으로 합침
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] = a

def checkSame(a, b):                                        # 같은 그룹에 속하는지 확인하는 함수
    a = find(a)
    b = find(b)
    if a==b:
        return True
    return False

for i in range(M):                                          # 각 파티에 참석한 사람들 입력받기
    party[i] = list(map(int, input().split()))
    del party[i][0]                                         # 첫번째 요소 삭제
    
parent = [0]*(N+1)                                          # 부모 리스트 초기화

for i in range(N+1):
    parent[i] = i
    
for i in range(M):                                          # 각 파티에 참석한 사람들 같은 그룹으로 묶음
    firstPeople = party[i][0]    
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])
        
for i in range(M):                                          # 각 파티가 거짓말 가능한 지 검사
    isPossible = True
    firstPeople = party[i][0]
    for j in range(len(trueP)):
        if find(firstPeople) == find(trueP[j]):             # 첫 참석자와 진실을 아는 사람이 같은 경우 
            isPossible = False                              # 거짓말 불가
            break
    if isPossible:
        result += 1
        
print(result)                                               # 거짓말 가능한 파티수 출력
