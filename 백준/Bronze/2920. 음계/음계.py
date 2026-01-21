arr = list(map(int, input().split()))
if arr[0] == 1:
    for i in range(1, 8):
        if arr[i] != arr[i-1] +1:
            ans = "mixed"
            break
        ans = "ascending"
elif arr[0] == 8:
    for i in range(1, 8):
        if arr[i-1] -1 != arr[i]:
            ans = "mixed"
            break
        ans = "descending"
else:
    ans = "mixed"
    
print(ans)