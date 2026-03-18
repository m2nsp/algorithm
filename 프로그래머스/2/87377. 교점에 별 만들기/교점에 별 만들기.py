def solution(line):
    points = []

    # 1. 교점 구하기
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]

            con = a * d - b * c
            if con == 0:
                continue

            x = (b * f - e * d) / con
            y = (e * c - a * f) / con

            if x.is_integer() and y.is_integer():
                points.append((int(x), int(y)))

    # 2. 범위 구하기
    minX = min(x for x, y in points)
    maxX = max(x for x, y in points)
    minY = min(y for x, y in points)
    maxY = max(y for x, y in points)

    # 3. 별 찍기
    answer = []
    for y in range(maxY, minY - 1, -1):
        s = ""
        for x in range(minX, maxX + 1):
            if (x, y) in points:
                s += "*"
            else:
                s += "."
        answer.append(s)

    return answer