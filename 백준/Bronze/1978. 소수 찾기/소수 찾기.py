n = int(input())
num_list = list(input().split())
cnt = 0

for i in range(len(num_list)):
    divisor = []
    for j in range(1, int(num_list[i]) + 1):
        if int(num_list[i]) % j == 0:
            divisor.append(j)

    if len(divisor) == 2:
        cnt += 1

print(cnt)