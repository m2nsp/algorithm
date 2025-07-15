import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
dq = deque()    # 덱 생성
for _ in range(N):
    data = list(input().split())
    if len(data)==1:
        if data[0] == 'pop_front':
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif data[0] == 'pop_back':
            if dq:
                print(dq.pop())
            else:
                print(-1)
        elif data[0] == 'size':
            print(len(dq))
        elif data[0] == 'empty':
            if dq:
                print(0)
            else:
                print(1)
        elif data[0] == 'front':
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif data[0] == 'back':
            if dq:
                print(dq[-1])
            else:
                print(-1)    
    elif len(data)==2:
        a = data[0]
        b = data[1]
        if a == 'push_front':
            dq.appendleft(b)
        elif a == 'push_back':
            dq.append(b)