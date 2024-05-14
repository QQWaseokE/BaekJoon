n = int(input())
result = []
for i in range(n):
    list_i = list(str(i))
    m = int(i)

    for j in range(0, len(list_i)):
        m += int(list_i[j])

    if m == n:
        result.append(i)

if len(result) == 0:
    print(0)
else:
    print(min(result))