N, M = map(int, input().split())
nums = list(range(1, N+1))
used = [False] * N

def backtracking(path):
    if len(path) == M:
        print(*path)
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            backtracking(path + [nums[i]])
            used[i] = False

backtracking([])