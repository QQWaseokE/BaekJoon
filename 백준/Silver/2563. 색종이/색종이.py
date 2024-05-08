rows = 100
cols = 100
paper = [[0 for j in range(cols)] for i in range(rows)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    for i in range(x - 1, x + 9):
        for j in range(y - 1, y + 9):
            paper[i][j] = 1

sum = 0
for i in range(100):
    sum += paper[i].count(1)

print(sum)