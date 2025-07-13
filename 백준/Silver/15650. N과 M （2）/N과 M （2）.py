N, M = map(int, input().split())
nums = list(range(1, N+1))
used = [False]*N

def backtracking(st, path):
    if len(path) == M:
        print(*path)
        return
    for i in range(st, N):
        if not used[i]:
            used[i] = True
            backtracking(i+1, path + [nums[i]])
            used[i] = False
backtracking(0, [])