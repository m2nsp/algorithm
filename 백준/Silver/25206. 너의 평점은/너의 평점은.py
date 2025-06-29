import sys
input = sys.stdin.readline

def get_d(c):
    if c == "A+":
        return 4.5
    elif c == "A0":
        return 4.0
    elif c == "B+":
        return 3.5        
    elif c == "B0":
        return 3.0
    elif c == "C+":
        return 2.5
    elif c == "C0":
        return 2.0
    elif c == "D+":
        return 1.5
    elif c == "D0":
        return 1.0
    elif c == "F":
        return 0.0

sum_b = 0 # 학점 합
sum_bd = 0 

for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c == 'P':
        continue
    d = get_d(c)
    sum_b += b
    sum_bd += b * d

avg = sum_bd / sum_b
print(avg)
