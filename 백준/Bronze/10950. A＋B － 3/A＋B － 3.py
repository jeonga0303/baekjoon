t = int(input())
result = []
for i in range(0, t):
    a, b = map(int, input().split())
    result.append(a+b)
    
for i in result:
    print(i)