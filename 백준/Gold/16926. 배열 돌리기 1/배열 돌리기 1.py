def rotate(x1, y1, x2, y2):
    layers = []     # 테두리 값들 저장
    
    for y in range(y1+1, y2+1):
        layers.append((x1, y))
    for x in range(x1+1, x2+1):
        layers.append((x, y2))
    for y in range(y2-1, y1-1, -1):
        layers.append((x2, y))
    for x in range(x2-1, x1-1, -1):
        layers.append((x, y1))  
    
    # 값 복사해두기 - 덮어쓰기 방지
    B = [A[r][c] for r, c in layers]
    
    for i in range(len(layers)):
        r, c = layers[(i - R) % len(layers)]
        A[r][c] = B[i]


N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 회전의 꼭짓점이 될 지점들 저장
points = []
st_r, st_c = 0, 0
end_r, end_c = N-1, M-1
while (end_r - st_r) >= 1 and (end_c - st_c) >= 1:
    points.append((st_r, st_c, end_r, end_c))
    st_r, st_c = st_r+1, st_c+1
    end_r, end_c = end_r-1, end_c-1
    
for p in points:
    x1, y1, x2, y2 = p
    rotate(x1, y1, x2, y2)
    
for i in range(N):
    for j in range(M):
        print(A[i][j], end=" ")
    print()
    