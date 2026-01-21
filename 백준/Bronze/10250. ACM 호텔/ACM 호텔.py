T = int(input())
test = [map(int, input().split()) for _ in range(T)]
for case in test:
    H, W, N = case
    floor = N % H
    room = N//H + 1
    
    # 예외 존재!
    if floor == 0:
        floor = H
        room = N//H
        
    print(f"{floor}{room:02d}")