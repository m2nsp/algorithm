import sys
input = sys.stdin.readline

st = list(input().strip())        #sys.stdin.readline()은 기본적으로 **문자열 끝에 \n(개행문자)**를 포함
i = int(input())
print(st[i-1])