n = int(input())
for i in range(n):
    m, s = input().split()
    m = int(m)
    s = str(s)
    for j in range(len(s)):
        print(m*s[j], end="")
    print()