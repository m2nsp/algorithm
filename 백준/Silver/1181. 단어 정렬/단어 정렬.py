import sys
input = sys.stdin.readline

N = int(input().strip())

s = []
for i in range(N):
    a = input().strip()
    s.append((len(a), a))
s = list(set(s))
s.sort(key=lambda x: (x[0], x[1]))

for l, word in s:
    print(word)