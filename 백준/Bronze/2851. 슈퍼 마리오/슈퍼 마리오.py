import sys

list = [int(sys.stdin.readline()) for _ in range(10)]
sum = 0

for i in range(10):
    sum += list[i]

    if i == 9:
        a = i
        break
    else:
        if sum + list[i + 1] > 100:
            a = i
            break

if a == 9:
    print(sum)
else:
    if 100 - sum < sum + list[a + 1] - 100:
        print(sum)
    elif 100 - sum >= sum + list[a + 1] - 100:
        print(sum + list[a + 1])
