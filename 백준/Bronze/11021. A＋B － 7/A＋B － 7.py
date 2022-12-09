t = int(input())
res = []
for i in range(0, t):
    a, b = map(int, input().split())
    res.append(a+b)
for i, j in enumerate(res):
    print('Case #{}: {}'.format(i+1, j))
