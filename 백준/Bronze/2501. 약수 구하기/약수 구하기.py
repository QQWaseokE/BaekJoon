a, b = map(int, input().split())
divisor = []

for i in range(1, a + 1):
    if a % i == 0:
        divisor.append(i)

n = len(divisor)

if n < b:
    print(0)
else:
    print(divisor[b - 1])