import sys
input = sys.stdin.readline

# 세그먼트 트리 생성
def build_segment_tree(arr, seg_tree, node, start, end):
    if start == end:
        seg_tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, seg_tree, 2 * node, start, mid)
        build_segment_tree(arr, seg_tree, 2 * node + 1, mid + 1, end)
        seg_tree[node] = min(seg_tree[2 * node], seg_tree[2 * node + 1])

# 최솟값을 찾는 함수
def find_min(seg_tree, node, start, end, left, right):
    if right < start or end < left:  # 구간이 겹치지 않는 경우
        return float('inf')
    if left <= start and end <= right:  # 구간이 완전히 포함되는 경우
        return seg_tree[node]
    mid = (start + end) // 2
    left_min = find_min(seg_tree, 2 * node, start, mid, left, right)
    right_min = find_min(seg_tree, 2 * node + 1, mid + 1, end, left, right)
    return min(left_min, right_min)

# 입력받기
N, M = map(int, input().split())  # N: 수의 개수, M: 질의 개수
A = [int(input()) for _ in range(N)]

# 세그먼트 트리 초기화
seg_tree = [0] * (4 * N)
build_segment_tree(A, seg_tree, 1, 0, N - 1)

# 쿼리 처리
for _ in range(M):
    a, b = map(int, input().split())
    print(find_min(seg_tree, 1, 0, N - 1, a - 1, b - 1))
