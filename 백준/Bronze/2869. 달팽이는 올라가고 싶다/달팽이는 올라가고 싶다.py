import math

a, b, v = map(int, input().split())

mid_day = v - a
day = math.ceil(mid_day / (a - b))

if v - (mid_day * (a - b)) <= a:
    day += 1

print(int(day))