import sys
input = sys.stdin.readline

A, B = list(input().split())
A = int(A[::-1])
B = int(B[::-1])
if(A>=B):
    print(A)
else:
    print(B)