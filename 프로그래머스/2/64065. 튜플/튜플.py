def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    data = sorted(s, key=lambda x: len(x))
    answer = []
    for item in data:
        item = list(map(int, item.split(",")))
        for value in item:
            if value not in answer:
                answer.append(value)
    return answer