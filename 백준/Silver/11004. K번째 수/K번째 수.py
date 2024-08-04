N, K = map(int, input().split())                          # N : 주어진 수의 개수 / K : 구하려는 수의 순서
  
A = list(map(int, input().split()))                       # A : 주어진 수들 저장하는 리스트

sorted_A = sorted(A)                                      # sorted_A : A를 오름차순으로 정렬한 결과 저장

print(sorted_A[K-1])
