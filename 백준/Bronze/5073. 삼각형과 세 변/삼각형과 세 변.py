while True:
    number = []
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        two_num = 0
        number.append(a)
        number.append(b)
        number.append(c)
        max_num = number.pop(number.index(max(number)))
        for i in range(0, 2):
            two_num += number[i]

        if two_num > max_num:
            if a == b == c:
                print("Equilateral")
            elif a == b and a != c:
                print("Isosceles")
            elif b == c and b != a:
                print("Isosceles")
            elif a == c and a != b:
                print("Isosceles")
            else:
                print("Scalene")
        else:
            print("Invalid")