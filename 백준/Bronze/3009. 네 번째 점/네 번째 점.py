X = []
Y = []
for _ in range(3):
    a, b = map(int, input().split())
    X.append(a)
    Y.append(b)
for i in range(3):
    if X.count(X[i]) == 1:
        x = X[i]
    if Y.count(Y[i]) == 1:
        y = Y[i]
print(x, end=' ')
print(y)