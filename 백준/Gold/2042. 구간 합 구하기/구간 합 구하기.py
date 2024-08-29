import sys
input = sys.stdin.readline

#세그먼트 트리 생성
def build_segment_tree(arr, seg_tree, node, start, end):
    if start == end:
        seg_tree[node] = arr[start]
    else:
        mid = (start+end)//2
        build_segment_tree(arr, seg_tree, 2*node, start, mid)
        build_segment_tree(arr, seg_tree, 2*node+1, mid+1, end)
        seg_tree[node] = seg_tree[2*node] + seg_tree[2*node+1]

# 구간 합 구하기
def range_sum(seg_tree, node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <=start and end <= right:
        return seg_tree[node]
    mid = (start+end)//2
    l_sum = range_sum(seg_tree, 2*node, start, mid, left, right)
    r_sum = range_sum(seg_tree, 2*node+1, mid+1, end, left, right)
    return l_sum + r_sum

# 값 업데이트
def update(seg_tree, node, start, end, idx, value):
    if start == end:
        seg_tree[node] = value
    else:
        mid = (start+end)//2
        if start <= idx <= mid:
            update(seg_tree, 2*node, start, mid, idx, value)
        else:
            update(seg_tree, 2*node+1, mid+1, end, idx, value)
        seg_tree[node] = seg_tree[2*node] + seg_tree[2*node+1]

#입력 받기
N, M, K = map(int, input().split())        # N: 수의 개수, M: 수의 변경이 일어나는 횟수, K: 구간합 구하는 횟수
A = [int(input()) for _ in range(N)]

#세그먼트 트리 초기화
seg_tree = [0]*(4*N)        # 세그먼트 트리는 완전 이진 트리일 경우 높이가 log2(N) --> 이는 2*N에서 4*N 사이임
build_segment_tree(A, seg_tree, 1, 0, N-1)

#처리
for _ in range(M+K):
    a, b, c  = map(int, input().split())
    # 값 변경
    if a==1:
        update(seg_tree, 1, 0, N-1, b-1, c)        # 인덱스 주의
    # 구간 합 출력
    else:
        print(range_sum(seg_tree, 1, 0, N-1, b-1, c-1))
                
