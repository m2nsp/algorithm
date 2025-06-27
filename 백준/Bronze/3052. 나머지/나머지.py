import sys
input = sys.stdin.readline

A = []
for _ in range(10):
    k = int(input())
    A.append(k)
    
for i in range(10):
    A[i] = A[i]%42
    

cnt = len(set(A))
print(cnt)