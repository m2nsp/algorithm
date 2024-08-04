N = int(input())                                        # N : 수의 개수

A = []                                                  # 주어진 수들 저장할 리스트 초기화
for _ in range(N):
    A.append(int(input()))

sorted_A = sorted(A)                                    # 오름차순으로 정렬

for i in range(N):
    print(sorted_A[i])
