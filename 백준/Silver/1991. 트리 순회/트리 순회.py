N = int(input())

nums = [input().split() for _ in range(N)]

tree = {}
for i in range(N):
    center = nums[i][0]
    left = nums[i][1]
    right = nums[i][2]
    tree[center] = [left, right]

# 1. 전위순회
def pre_trav(center):
    if center == '.':
        return
    print(center, end='') #center
    pre_trav(tree[center][0]) #left
    pre_trav(tree[center][1]) #right
    
# 2. 중위순회   
def in_trav(center):
    if center == '.':
        return
    in_trav(tree[center][0]) #left
    print(center, end='') #center
    in_trav(tree[center][1]) #right

# 3. 후위순회
def post_trav(center):
    if center == '.':
        return
    post_trav(tree[center][0]) #left
    post_trav(tree[center][1]) #right
    print(center, end='') #center
    
pre_trav('A'); print()
in_trav('A'); print()
post_trav('A')