import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum = [0]
temp = 0

for i in numbers:
    temp += i
    sum.append(temp)
    
for i in range(M):
    s, e = map(int, input().split())
    print(sum[e] - sum[s-1])

"""
합배열 사용한 다른 코드와 실행시간에 차이가 많이 나는 이유
1. 입력 방법
input() 보다 sys.stdin.readline 이 좀 더 효율적인 방식임
2. 출력 방법
반복문 마다 print 함수를 사용하는 것 보다 sys.stdout.write 를 사용하여 한번에 출력을 모아서 처리하는 것이 더 좋음
"""
