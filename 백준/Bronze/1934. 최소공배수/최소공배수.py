def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

N = int(input())                        #테스트 케이스 개수

for _ in range(N):
    A, B = map(int, input().split())
    result = A * B // gcd(A, B)  
    print(result)
