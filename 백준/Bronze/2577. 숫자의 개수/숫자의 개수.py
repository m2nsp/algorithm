A, B, C = [int(input()) for _ in range(3)]

num = A * B * C

str_num = str(num)
for i in range(10):
    cnt = str_num.count(str(i))
    print(cnt)
    