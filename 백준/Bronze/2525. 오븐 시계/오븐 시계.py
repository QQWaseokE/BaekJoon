H, M = map(int,input().split())
n = int(input())

minute = M+n

while minute>=60:
    if (minute>=60):
        H += 1
        minute -= 60
        if (H==24):
            H = 0

print(H, minute)