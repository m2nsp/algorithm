mod = 10007
N = int(input())
D = [0]*(1001)
D[1] = 1    # 길이가 2*1인 경우
D[2] = 2    # 길이가 2*2인 경우

for i in range(3, N+1):
    D[i] = (D[i-1] + D[i-2]) % mod    # 점화식
    
print(D[N])