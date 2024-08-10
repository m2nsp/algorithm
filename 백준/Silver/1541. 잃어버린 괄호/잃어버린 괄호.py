A = list(map(str, input().split("-")))

total_sum = 0

for i in range(len(A)):
    B = A[i].split("+")
    for item in B:
        if i == 0:
            total_sum += int(item)
        else:
            total_sum -= int(item)

print(total_sum)
