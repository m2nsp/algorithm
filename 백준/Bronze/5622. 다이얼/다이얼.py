import sys
input = sys.stdin.readline

groups = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input().strip()
time = 0

for ch in S:
    for i in range(len(groups)):
        if ch in groups[i]:
            time += (i+3)
            break
print(time)