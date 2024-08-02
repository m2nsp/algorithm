import sys
input = sys.stdin.readline

n, m = map(int, input().split())                                        # n: 표 크기, m: 합 횟수

A = [[0]* (n+1)]                                                        # 주어진 수 받을 배열          
D = [[0]* (n+1) for _ in range(n+1)]                                    # 합 배열        

for i in range(n):                                                      # 주어진 수들 저장하기         
    A_row = [0] + [int(x) for x in input().split()]                             
    A.append(A_row)

for i in range(1, n+1):                                                 # 합배열 공식 이용해서 계산하기
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]                  


for _ in range(m):                                                      # 구간의 합 구하기
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]              
    print(result)