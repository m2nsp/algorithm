import sys
input = sys.stdin.readline

N = int(input().strip())
s = []  #튜플 저장할 배열
for _ in range(N):
	a, b = input().split()
	s.append((int(a), b))
sorted_s = sorted(s, key = lambda x: x[0])
	
for age, name in sorted_s:
    print(age, name)