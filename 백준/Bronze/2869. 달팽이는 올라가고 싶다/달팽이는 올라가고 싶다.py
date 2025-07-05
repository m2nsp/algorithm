A, B, V = map(int, input().split())
target = V-A
day = 0
# 반복문 사용하면 시간초과!
if target % (A-B) == 0:
    day = target // (A-B)
else:
    day = target // (A-B) + 1
print(day + 1)