n = int(input())
num = n
count = 0
while True:
    a = num // 10 # 6
    b = num % 10 # 8
    c = (a+b) % 10 # 6 + 8 = 1'4'
    num = (b * 10) + c # 80 + 4 = 84
    count += 1
    if (num == n):
        break
print(count)