n = int(input())
a = 3

for i in range(n):
    if i == 0:
        a = 3
    else:
        a = a + (a - 1)
    result = a**2

print(result)