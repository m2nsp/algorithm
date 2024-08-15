# 오일러 피함수 이용해서 푸는 문제
import math
N = int(input())
result = N

for p in range(2, int(math.sqrt(N)) + 1):
    if N % p == 0:
        result -= result/p
        while N % p == 0:
            N /= p
            
if N > 1:
    result -= result/N
    
print(int(result))


# 아직 이해를 다 못해서 다시보기..........****
