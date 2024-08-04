import sys
input = sys.stdin.readline

N = int(input())                        # N : 배열의 크기
A = []                                  # A : 정렬 대상 배열

for i in range(N):
    A.append((int(input()), i))         # 주어진 수들 저장

Max = 0                                 # 원래 배열의 인덱스와 정렬된 배열의 인덱스 차이의 최댓값을 저장하는 변수
sorted_A = sorted(A)                    # 배열 정렬 수행

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max+1)


"""
C코드와 똑같이 구현하면 버블 정렬을 사용하여 배열을 정렬하는 것이다. 버블 정렬의 경우 시간 복잡도는 O(N^2)이다.
두번째 코드는 배열을 한 번 정렬하고, 원래의 인덱스와 정렬 후의 인덱스 차이를 계산하여 최댓값을 구하는 방법이다. 이 경우 시간 복잡도는 O(NlogN)이다.
"""