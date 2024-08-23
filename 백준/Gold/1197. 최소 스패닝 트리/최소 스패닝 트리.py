import sys
from queue import PriorityQueue

input = sys.stdin.readline

# N: 정점의 수, M: 간선의 수
N, M = map(int, input().split())

# 우선순위 큐를 이용해 간선을 가중치 기준으로 정렬하기 위해 PriorityQueue를 사용
pq = PriorityQueue()

# 부모 노드를 저장할 리스트 초기화 (각 정점이 자기 자신을 부모로 가짐)
parent = [0] * (N + 1)

# 초기화: 각 정점이 자기 자신을 부모로 갖도록 설정
for i in range(N + 1):
    parent[i] = i

# 간선 정보를 입력받아 우선순위 큐에 삽입
for i in range(M):
    s, e, w = map(int, input().split())  # s: 시작 정점, e: 끝 정점, w: 가중치
    pq.put((w, s, e))  # 가중치를 기준으로 우선순위 큐에 삽입 (오름차순 정렬)

# 특정 정점의 대표(parent)를 찾는 함수 (경로 압축 기법 사용)
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])  # 경로 압축
        return parent[a]

# 두 정점을 하나의 집합으로 합치는 함수 (union by rank를 사용하지 않음)
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a  # 두 정점을 연결 (b의 부모를 a로 설정)

# 최소 스패닝 트리를 만들기 위한 변수들 초기화
useEdge = 0  # 사용된 간선의 수
result = 0  # 최소 스패닝 트리의 총 가중치

# 크루스칼 알고리즘 실행
while useEdge < N - 1:  # MST는 항상 N-1개의 간선을 가짐
    w, s, e = pq.get()  # 가중치가 가장 작은 간선부터 선택
    if find(s) != find(e):  # 사이클을 만들지 않는다면
        union(s, e)  # 두 정점을 연결
        result += w  # MST의 총 가중치에 더함
        useEdge += 1  # 사용된 간선 수 증가

# 최소 스패닝 트리의 총 가중치를 출력
print(result)
