N = int(input())                    # 숫자의 개수
A = list(input())                   # 숫자들 받는 수
sum = 0                             # 합 변수 초기화

for item in A:
    sum += int(item)                # 반복문 돌면서 합 구하기

print(sum)                          # 합 출력