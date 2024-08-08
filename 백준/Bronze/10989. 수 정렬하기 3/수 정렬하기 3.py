import sys
input = sys.stdin.readline
N = int(input())                        # N : 수의 개수
count = [0]*10001                       # 주어진 수의 개수 저장할 배열 초기화

for i in range(N):
    count[int(input())] += 1            # 주어진 수를 인덱스로 하는 count배열에 수 +1
   
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):       # count[i]는 i가 주어진 개수이므로 그만큼 출력
            print(i)
            
# 복습 필요!!
# N의 최대 개수가 매우 크므로 O(nlogn) 보다 더 빠른 알고리즘이 필요하다는 것 인지 필요!