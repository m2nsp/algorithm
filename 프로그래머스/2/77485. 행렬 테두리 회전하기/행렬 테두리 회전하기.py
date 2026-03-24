def solution(rows, columns, queries):
    
    # 첫 배열 초기화
    A = [[] for _ in range(rows)]
    for r in range(rows):
        for c in range(1, columns+1):
            A[r].append((r*columns)+c)
    
    answer = []
    for q in queries:
        v = rotate(A, q)
        answer.append(v)
    
    return answer

def rotate(A, q):
    x1, y1, x2, y2 = q
    
    points = [] # 회전 대상 지점들
    for y in range(y1, y2):
        points.append((x1, y))
    for x in range(x1, x2):
        points.append((x, y2))
    for y in range(y2, y1, -1):
        points.append((x2, y))
    for x in range(x2, x1, -1):
        points.append((x, y1))
    
    # 값 복사해두기 - 덮어쓰기 방지
    values = [A[r-1][c-1] for r, c in points]
    
    # 시계방향으로 1만큼씩 회전하기
    for i in range(len(points)):
        r, c = points[(i+1)% len(points)]
        A[r-1][c-1] = values[i]
    
    minV = min(v for v in values)
    return minV
    
        