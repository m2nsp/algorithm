A = list(map(str, input().split("-")))                                    # A: 주어진 문자열 -를 기준으로 쪼개서 받아옴

total_sum = 0                                                             # 최종 합

for i in range(len(A)):
    B = A[i].split("+")                                                   # 쪼개진 요소들을 다시 +를 기준으로 나눔
    for item in B:
        if i == 0:                                                        # 첫 요소는 더함
            total_sum += int(item)
        else:                                                             # 나머지 요소는 뺌
            total_sum -= int(item)

print(total_sum)
