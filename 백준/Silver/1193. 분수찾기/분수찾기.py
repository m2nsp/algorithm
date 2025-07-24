line = 0
s = 0
X = int(input())
while X > s:
    line += 1
    s += line
a = s - X

if line % 2 == 0:
    front = line-a
    back = 1+a
else:
    front = 1+a
    back = line - a 

print(f"{front}/{back}")