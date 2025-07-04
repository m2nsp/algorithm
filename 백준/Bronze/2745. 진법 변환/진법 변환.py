N, B =input().split()
list_N = list(N)[::-1]
int_B = int(B)
s = 0
for i in range(len(list_N)):
    j = int_B ** i
    k = ord(list_N[i])
    if k < 65:  #숫자
        k = k-48
    elif k < 97:
        k = (k - 65)+10  # 대문자
    s += k * j
print(s)