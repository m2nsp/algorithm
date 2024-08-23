import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M = map(int, input().split())                                # N: 정점의 수, M: 간선의 수

# 우선순위 큐를 이용해 간선을 가중치 기준으로 정렬하기 위해 PriorityQueue를 사용
pq = PriorityQueue()

parent = [0] * (N + 1)                                          # 부모 노드를 저장할 리스트 초기화

for i in range(N + 1):                                          # 초기화: 각 정점이 자기 자신을 부모로 갖도록 설정
    parent[i] = i

for i in range(M):                                              # 간선 정보를 입력받아 우선순위 큐에 삽입
    s, e, w = map(int, input().split())                         # s: 시작 정점, e: 끝 정점, w: 가중치
    pq.put((w, s, e))                                           # 가중치를 기준으로 우선순위 큐에 삽입 (오름차순 정렬)

def find(a):                                                    # 특정 정점의 대표(parent)를 찾는 함수 
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):                                                # 두 정점을 하나의 집합으로 합치는 함수
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a  # 두 정점을 연결 (b의 부모를 a로 설정)

# 최소 스패닝 트리를 만들기 위한 변수들 초기화
useEdge = 0                                                     # 사용된 간선의 수
result = 0                                                      # 최소 스패닝 트리의 총 가중치

# 크루스칼 알고리즘
while useEdge < N - 1:                                          # MST는 항상 N-1개의 간선을 가짐
    w, s, e = pq.get()                                          # 가중치가 가장 작은 간선부터 선택
    if find(s) != find(e):                                      # 사이클을 만들지 않는다면, 두 정점 연결
        union(s, e) 
        result += w 
        useEdge += 1  

# 최소 스패닝 트리의 총 가중치를 출력
print(result)
