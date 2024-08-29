import sys
input = sys.stdin.readline

MOD = 1000000007  # 큰 수로 나누기 위한 MOD 값 설정

# 세그먼트 트리 생성
def build_segment_tree(arr, seg_tree, node, start, end):
    if start == end:
        seg_tree[node] = arr[start] % MOD
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, seg_tree, 2 * node, start, mid)
        build_segment_tree(arr, seg_tree, 2 * node + 1, mid + 1, end)
        seg_tree[node] = (seg_tree[2 * node] * seg_tree[2 * node + 1]) % MOD

# 구간 곱 구하기
def range_multiple(seg_tree, node, start, end, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end) // 2
    l_prod = range_multiple(seg_tree, 2 * node, start, mid, left, right)
    r_prod = range_multiple(seg_tree, 2 * node + 1, mid + 1, end, left, right)
    return (l_prod * r_prod) % MOD

# 값 업데이트
def update(seg_tree, node, start, end, idx, value):
    if start == end:
        seg_tree[node] = value % MOD
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update(seg_tree, 2 * node, start, mid, idx, value)
        else:
            update(seg_tree, 2 * node + 1, mid + 1, end, idx, value)
        seg_tree[node] = (seg_tree[2 * node] * seg_tree[2 * node + 1]) % MOD

# 입력 받기
N, M, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# 세그먼트 트리 초기화
seg_tree = [1] * (4 * N)        
build_segment_tree(A, seg_tree, 1, 0, N - 1)

# 처리
output = []
for _ in range(M + K):
    a, b, c  = map(int, input().split())
    # 값 변경
    if a == 1:
        update(seg_tree, 1, 0, N - 1, b - 1, c)
    # 구간 곱 출력
    else:
        output.append(str(range_multiple(seg_tree, 1, 0, N - 1, b - 1, c - 1)))

# 한 번에 출력
sys.stdout.write("\n".join(output) + "\n")
