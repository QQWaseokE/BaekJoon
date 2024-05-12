x = int(input())

for i in range(2, x + 1):
    while x % i == 0:
        x = x / i
        print(i)