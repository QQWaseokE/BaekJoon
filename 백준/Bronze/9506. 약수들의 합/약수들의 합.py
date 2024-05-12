while True:
    num = int(input())
    divisor = []
    sum = 0
    divisor_list = ""
    if num == -1:
        break
    else:
        for i in range(1, num):
            if num % i == 0:
                divisor.append(i)

        for i in range(len(divisor)):
            sum += divisor[i]
            if i != (len(divisor) - 1):
                divisor_list += str(divisor[i])
                divisor_list += " + "
            else:
                divisor_list += str(divisor[i])

        if num == sum:
            print(num, "=", divisor_list)
        else:
            print(f"{num} is NOT perfect.")