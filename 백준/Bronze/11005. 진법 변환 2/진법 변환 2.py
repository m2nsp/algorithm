N, B =map(int, input().split())
i = 0
C = []
while N > 0:
    C.append(N % B) #나머지
    N //= B #몫
C.reverse()
ans = []
for num in C:
    if num >= 10:
        ans.append(chr(55+num))
    else:
        ans.append(str(num))
result = ''.join(ans)
print(result)