import math
Min, Max = map(int, input().split())
A = [0]*(10000001)

for i in range(2, len(A)):
    A[i] = i
    
for i in range(2, int(math.sqrt(len(A)) + 1)):        #제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i):
        A[j] = 0
        
cnt = 0                                                # 거의 소수의 개수 저장하는 변수

for i in range(2, 10000001):
    if A[i]!=0:
        temp = A[i]
        while A[i] <= Max/temp:
            if A[i] >= Min/temp:
                cnt += 1
            temp = temp * A[i]
            
print(cnt)

"""
교재 참고함 - 직접 인덱스를 통해 바로 계산하는 방법인듯
"""
