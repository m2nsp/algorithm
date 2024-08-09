import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())                                            # N : 자리 수

def isPrime(num):                                           # 소수인지 확인하는 함수
    if num < 2:                                            
        return False
    for i in range(2, int(num ** 0.5) + 1):                 # 소수인지 확인만 하면되므로 나누어 떨어지는 경우가 존재하기만 하면 되는데, 만일 num = i * j 라하면 작은 쪽의 약수는 루트num 보다 클 수 없기 때문
        if num % i == 0:
            return False
    return True

def dfs(num):                                               # dfs를 통해서 일의 자리 수 일때부터 자리수를 늘려가면서 소수인지 검사
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(num * 10 + i):
                dfs(num * 10 + i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)

"""
계속 n자리수 일때부터 한자리씩 줄어들게 생각하는 경우만 생각했는데 반대로 생각해야한다는 것을 깨달았다...
"""
