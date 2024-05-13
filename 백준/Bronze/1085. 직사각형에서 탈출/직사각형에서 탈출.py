x, y, w, h = map(int, input().split())

w2 = w / 2
h2 = h / 2

if x < w2:
    a = x
else:
    a = w - x

if y < h2:
    b = y
else:
    b = h - y

print(min(a, b))