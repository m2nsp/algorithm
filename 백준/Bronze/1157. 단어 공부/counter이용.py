import Counter from collections
import sys
input = sys.stdin.readline

S = input().strip().upper()
counter = Counter(S)  

most_common = counter.most_common(2)  # [('A', 3), ('B', 2), ...] 식으로 정렬됨
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
  print('?')
else:
  print(most_common[0][0])
