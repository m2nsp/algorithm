N = int(input())                                    #시험을 본 과목의 개수
A = [0]*N                                           #새로운 성적을 저장할 리스트
scores = list(map(int, input().split()))            #주어진 성적값 읽어옴
M = max(scores)                                     #성적중 최고 성적

A = [score / M * 100 for score in scores]           #새로운 성적 계산해서 저장

sum = 0
for i in range(N):
    sum += A[i]                                     #평균 구하기 위한 합 구하기

avg = sum/N                                         #평균 구하기

print(avg)                                          #출력


"""
max() 함수는 리스트의 최댓값을 구하는 함수
sum() 함수를 이용하여 합도 간단하게 구할 수 있음
"""