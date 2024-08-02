import sys
input = sys.stdin.readline                        #입력
N = int(input())                                  #수의 개수
answer = 0                                        #좋은 수의 개수 저장 변수 초기화
A = list(map(int, input().split()))               #주어진 N개의 수
A.sort()                                          #오름차순으로 정렬

for k in range(N):
    find = A[k]                                    #찾아야 할 수
    i = 0                                         #i, j는 양 끝의 인덱스
    j = N-1
    while i<j: #투포인터 알고리즘
        if A[i] + A[j] == find:                    # A[i], A[j]의 합이 find일때,
            if i != k and j !=k:                  # i와 j 둘다 k가 아닐 때
                answer +=1                        # 좋은 수 개수 +1
                break
            elif i == k:                          # i나 j가 k일때 값 변경
                i +=1
            elif j == k:
                j -=1
        elif A[i] + A[j] < find:                    
            i +=1
        else:                                     # A[i] + A[j]가 find보다 큰 경우
            j-=1                                  # j를 줄여 합을 줄임

print(answer)