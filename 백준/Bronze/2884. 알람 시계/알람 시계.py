h, m = map(int, input().split())
# 10 10 => 9 25
if m < 45: # 45분보다 작으면 h에서 1을 빼준다.
    # 만약 h가 0이면 24를 더해줘야한다.
    if h == 0:
        h = 23
        m += 60
    else:
        h -= 1
        m += 60
print(h, m-45)