def push(nums, n):
    res = []
    for i in nums:
        if i == 32: # 공백
            res.append(32)
        elif 65 <= i <= 90 and (i + n) > 90:
            res.append(i+n-26)
        elif i >= 97 and (i + n) > 122:
            res.append(i+n-26)
        else:
            res.append(i + n)
    return res

def solution(s, n):
    nums = list(map(lambda x: ord(x), s))
    code = push(nums, n)
    return ''.join(map(chr, code))