import math
n = int(input())                                            # 주어진 수 n

def is_prime(n):                                            # n이 소수인지 확인하는 함수
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_pelindrom(n):                                        # 펠린드롬인지 확인하는 함수
    n  = str(n)                                             # 숫자로는 슬라이싱 이용할 수 없음 => 문자열, 튜플, 리스트와 같은 자료형에만 사용가능
    return n == n[::-1]

num = n                                                     # n이상의 값이므로 n으로 초기화

while True:
    if (is_prime(num) and is_pelindrom(num)):
        break
    else:
        num+=1

print(num)
