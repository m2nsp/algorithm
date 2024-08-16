A, B = map(int, input().split())

def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

gcd_length = gcd(A, B)
print('1' * gcd_length)
