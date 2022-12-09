user = map(int, input().split())
chess = [1,1,2,2,2,8]
res = []
for idx, item in enumerate(user):
    if item == chess[idx]:
        res.append(0)
    else:
        res.append(chess[idx]-item)
print(*res)