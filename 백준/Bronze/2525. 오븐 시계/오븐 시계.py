h, m = map(int, input().split())
cook_m = int(input())
cooking_time = m + cook_m
if cooking_time / 60 > 0: # 1시간을 넘는 경우
    plus_h, plus_m = divmod(cooking_time, 60)
    h += plus_h
    m = plus_m
    if h > 23:
        h -= 24
    print(h,m)
else: # 1시간을 넘지 않는 경우 (분 단위일 때)
    print(h,cooking_time)