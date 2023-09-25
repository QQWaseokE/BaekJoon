str = list(input())
n = len(str)
sum = 0

for i in range(n):
    if(str[i] == 'A' or str[i] == 'B' or str[i] == 'C'):
        str[i] = 3
    elif(str[i] == 'D' or str[i] == 'E' or str[i] == 'F'):
        str[i] = 4
    elif(str[i] == 'G' or str[i] == 'H' or str[i] == 'I'):
        str[i] = 5
    elif(str[i] == 'J' or str[i] == 'K' or str[i] == 'L'):
        str[i] = 6
    elif(str[i] == 'M' or str[i] == 'N' or str[i] == 'O'):
        str[i] = 7
    elif(str[i] == 'P' or str[i] == 'Q' or str[i] == 'R' or str[i] == 'S'):
        str[i] = 8
    elif(str[i] == 'T' or str[i] == 'U' or str[i] == 'V'):
        str[i] = 9
    elif(str[i] == 'W' or str[i] == 'X' or str[i] == 'Y' or str[i] == 'Z'):
        str[i] = 10
    else:
        str[i] = 2

for i in range(n):
    sum += str[i]
    
print(sum)