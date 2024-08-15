import sys
import math

input = sys.stdin.readline
min_value, max_value = map(int, input().split())

S = []  # 제곱수들 저장할 변수
for i in range(2, int(math.sqrt(max_value)) + 1):
    S.append(i * i)

# A 리스트는 min_value에서 max_value까지의 범위를 다룸
A = [1] * (max_value - min_value + 1)

# 제곱수의 배수들을 0으로 설정
for item in S:
    start = max(item, (min_value + item - 1) // item * item)
    for i in range(start, max_value + 1, item):
        A[i - min_value] = 0

# 남아있는 1의 개수를 카운트
cnt = 0
for i in range(len(A)):
    if A[i] == 1:
        cnt += 1

print(cnt)
