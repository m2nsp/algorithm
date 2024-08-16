A, B = map(int, input().split())            # A, B의 길이

def gcd(A, B):                              # 최대 공약수 구하는 함수
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

gcd_length = gcd(A, B)                      # 1로 이루어진 수에서의 최대공약수는 각 숫자의 길이의 최대공약수만큼의 1을 가진 수가 됨
print('1' * gcd_length)

"""
문자열로 각 숫자를 생성해서 정수로 바꾸는 방법 -- 바꾸는 과정에서 아주 큰 수가 생성될 수 있어 메모리 초과가 발생할 수 있음
"""
