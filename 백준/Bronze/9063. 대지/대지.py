n = int(input())
x = []
y = []

if n == 1:
    a, b = map(int, input().split())
    print("0")

else:
    for i in range(0, n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    print((max(x) - min(x)) * (max(y) - min(y)))