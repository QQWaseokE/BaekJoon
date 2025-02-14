import sys

num = input()

if int(num) == 0:
    sum = 1
else:
    if int(num) < 10:
        list_num = [0] * 2
        list_num[1] = int(num)
    else:
        list_num = list(map(int, str(num)))

    result_num = 0
    sum = 0

    while int(num) != result_num:
        if 0 < int(result_num) < 10:
            list_num = [0] * 2
            list_num[1] = int(result_num)
        else:
            list_num = list_num

        first_num = int(list_num[1])
        second = int(list_num[0] + list_num[1])

        if int(second) < 10:
            second_num = [0] * 2
            second_num[1] = int(second)
        else:
            second_num = list(map(int, str(second)))

        result_num = first_num * 10 + second_num[1]
        list_num = list(map(int, str(result_num)))

        sum += 1

print(sum)
