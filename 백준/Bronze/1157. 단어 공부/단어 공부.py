def find_max(a):
    string_list = list(set(a))
    string_number = []
    for i in string_list:
        string_number.append(string.count(i))

    n = len(string_number)
    result = 0
    expt = 0

    if n == 1:
        print(string_list[0])

    else:
        for i in range(0, n):
            for j in range(i + 1, n):
                if string_number[i] == string_number[j]:
                    if string_number[i] >= max(string_number):
                        expt += 1
                    else:
                        result = max(string_number)
                else:
                    result = max(string_number)

        if expt > 0:
            print("?")
        else:
            print(string_list[string_number.index(result)])


string = input().upper()
find_max(string)
