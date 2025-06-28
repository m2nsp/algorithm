def is_pelindrome(S):
    rev_S = S[::-1]
    if(rev_S == S):
        return 1
    else:
        return 0
        
S = input()
print(is_pelindrome(S))