x = int(input())

for n in range(1, 1000000):
    if x == 1:
        print(1)
        break
    elif ((((n - 1) * n) / 2) * 6) + 1 < x <= (((n * (n + 1)) / 2) * 6) + 1:
        print(n + 1)