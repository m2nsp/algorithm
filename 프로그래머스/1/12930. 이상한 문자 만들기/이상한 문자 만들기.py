def solution(s):
    s = s.split(' ')
    
    for j in range(len(s)):
        s[j] = list(s[j])
        for i in range(len(s[j])):
            if i % 2 !=0:
                s[j][i] = s[j][i].lower()
            else:
                s[j][i] = s[j][i].upper()
        s[j] = ''.join(s[j])
    res = ' '.join(s)
    
    return res