import math
n = int(input())

def is_prime(n):                                            # n이 소수인지 확인하는 함수
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_pelindrom(n):
    n  = str(n)
    return n == n[::-1]

num = n

while True:
    if (is_prime(num) and is_pelindrom(num)):
        break
    else:
        num+=1

print(num)