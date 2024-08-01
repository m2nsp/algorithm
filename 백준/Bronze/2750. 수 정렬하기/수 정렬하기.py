N = int(input())                                        # 첫 번째 줄의 수의 개수 N 읽어옴
A = [0]*N                                               # N개의 숫자를 저장할 배열 초기화
for i in range(N):
    A[i] = int(input())                                 # N개의 숫자 저장

A.sort()                                                # A 오름차순 정렬

for item in A:                                          # 앞에서 부터 A 출력
    print(item, end=' ')
