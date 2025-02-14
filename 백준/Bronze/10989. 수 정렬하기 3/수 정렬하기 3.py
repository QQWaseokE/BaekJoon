import sys

n = int(sys.stdin.readline())
list = [0] * 10001

for _ in range(n):
    list[int(sys.stdin.readline())] += 1

for i in range(len(list)):
    while list[i] != 0:
        print(i)
        list[i] -= 1
