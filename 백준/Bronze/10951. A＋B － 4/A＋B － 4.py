import sys
input = sys.stdin.readline

while True:
    try:
        i, j = map(int, input().split())
    except:
        break
    print(i+j)