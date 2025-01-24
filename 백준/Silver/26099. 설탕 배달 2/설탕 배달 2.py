import sys

n = int(input())
m1 = n % 5
a = n // 5


if m1 == 0:
    print(a)

else:
    for i in range(0, a + 1):
        m = n - (5 * (a - i))
        if m % 3 == 0:
            print((a - i) + (m // 3))
            sys.exit()
    print(-1)
