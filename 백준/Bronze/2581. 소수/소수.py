a = int(input())
b = int(input())
result = []
sum = 0

for i in range(a, b + 1):
    divisor = []
    for j in range(1, i + 1):
        if i % j == 0:
            divisor.append(j)

    if len(divisor) == 2:
        result.append(i)

for x in range(len(result)):
    sum += result[x]

if len(result) == 0:
    print("-1")
else:
    print(sum)
    print(result[0])