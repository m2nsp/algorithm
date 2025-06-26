import sys
input = sys.stdin.readline

A = [0]*31
for _ in range(28):
    k = int(input())
    A[k] = k
    
ans = []
for i in range(1, 31):
    if A[i] == 0:
        ans.append(i)
ans.sort()
for num in ans:
    print(num)