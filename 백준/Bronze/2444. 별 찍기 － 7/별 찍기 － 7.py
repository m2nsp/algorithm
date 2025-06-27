import sys
input = sys.stdin.readline

T = int(input().strip())
for i in range(1, T+1):
    print((T-i)*' ' + i*'*'+ '*'*(i-1))
    
for i in range(T-1, 0, -1):
    print((T-i)*' ' + i*'*'+ '*'*(i-1))
    