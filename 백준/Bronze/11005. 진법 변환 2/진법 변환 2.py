n, b = map(int, input().split())
result = ""

while n != 0:
    a = n % b
    if a >= 10:
        result += chr(a + 55)
    else:
        result += str(a)
    n = n // b

print(result[::-1])