arr = []


for i in range(0, 9):
    arr.append(list(map(int, input().split())))

a, b, c = 1, arr[0].index(max(arr[0])) + 1, max(arr[0])

for i in range(0, 9):
    for j in range(i + 1, 9):
        if c < max(arr[j]):
            a, b, c = j + 1, arr[j].index(max(arr[j])) + 1, max(arr[j])

print(c)
print(a, b)