from collections import Counter
import sys
input = sys.stdin.readline
ar = []
for _ in range(5):
    ar.append(int(input().strip()))
    
cnt = Counter(ar)
for k,v in cnt.items():
    if v % 2 == 1:
        print(k)
        break