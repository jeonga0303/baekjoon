import sys
t = sys.stdin.readline().rstrip()
res = []
for i in range(0, int(t)):
    line = sys.stdin.readline().rstrip()
    a, b = map(int, line.split())
    res.append(a+b)
for i in res:
    print(i)