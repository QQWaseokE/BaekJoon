def star(a):
    for i in range(1, a + 1):
        print(" " * (a - i) + "*" * ((2 * i) - 1))
    for i in range(a, 1, -1):
        print(" " * ((a + 1) - i) + "*" * ((2 * (i - 1)) - 1))


number = int(input())
star(number)