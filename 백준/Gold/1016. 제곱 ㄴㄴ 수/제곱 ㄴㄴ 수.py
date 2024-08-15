import sys
import math

input = sys.stdin.readline
min, max = map(int, input().split())                                # 최솟값, 최댓값 읽어오기

S = []                                                              # 제곱수들 저장할 리스트
for i in range(2, int(math.sqrt(max)) + 1):                         # sqrt() 함수는 실수를 반환함!! 주의
    S.append(i * i)
 
A = [1] * (max - min + 1)                                           # A 리스트는 제곱수의 배수인지 아닌지를 저장하는 리스트

for item in S:                                                      # 제곱수의 배수들을 0으로 설정
    start = max(item, ((min + item - 1) // item) * item)            # min 보다 커아하는 조건
    for i in range(start, max + 1, item):
        A[i - min] = 0

cnt = 0                                                             # cnt는 제곱수의 배수가 아닌수의 개수를 저장하는 변수
for i in range(len(A)):                                             # 남아있는 1의 개수를 카운트
    if A[i] == 1:
        cnt += 1

print(cnt)
