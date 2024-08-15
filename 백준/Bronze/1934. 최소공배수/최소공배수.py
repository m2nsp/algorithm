def gcd(A, B):                        # 최대 공약수 구하는 함수 (재귀 이용)
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

N = int(input())                      # 테스트 케이스 개수

for _ in range(N):
    A, B = map(int, input().split())
    result = A * B // gcd(A, B)       # 수학적인 성질에 따라 -- 최소 공배수는 두 수의 곱을 그들의 최대 공약수로 나누어 구할 수 있음
    print(result)
