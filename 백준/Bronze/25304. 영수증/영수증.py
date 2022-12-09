x = int(input())
n = int(input())
price = []
for i in range(0, n):
    a, b = map(int, input().split())
    price.append(a*b)
res = 0
for i in price:
    res += i
if x == res:
    print('Yes')
else:
    print('No')