N = int(input())
mod = 1000000000
D = [0]*1000001        # 선물을 교환할 수 있는 모든 경우의 수 저장 리스트
D[1] = 0    # 혼자서 선물 교환 불가능
D[2] = 1    # 2명일 경우 서로 선물 교환

for i in range(3, N+1):
    D[i] = (i-1)*(D[i-1] + D[i-2]) % mod        # 완전 순열 점화식
    
print(D[N])
