n = int(input())
str = input()
array = list(str)
sum=0

for i in range(n):
    sum += int(array[i])

print(sum)