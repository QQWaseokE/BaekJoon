array = [0] * 10

for i in range(10):
    n = int(input())
    array[i] = n%42

count = list(set(array))

print(len(count))