n = int(input())
col = 4
result = [[0 for j in range(col)] for i in range(n)]

for i in range(n):
    money = int(input())

    for j in range(col):
        if j == 0:
            result[i][j] = money // 25
            money = money % 25
        elif j == 1:
            result[i][j] = money // 10
            money = money % 10
        elif j == 2:
            result[i][j] = money // 5
            money = money % 5
        elif j == 3:
            result[i][j] = money // 1
            money = money % 1

for a, b, c, d in result:
    print(a, b, c, d)