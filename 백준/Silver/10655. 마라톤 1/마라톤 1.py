N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

def compute(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])

total = 0  # 전체 거리
for i in range(N-1):
    total += compute(points[i], points[i+1])
    
# 최대 감소량 찾기
decreased = 0
for i in range(1, N-1):
    # 원래 거리
    origin = compute(points[i-1], points[i]) + compute(points[i], points[i+1])
    # 바뀐 거리
    changed = compute(points[i-1], points[i+1])
    # 차이
    decreased = max(decreased, origin - changed)
print(total - decreased)