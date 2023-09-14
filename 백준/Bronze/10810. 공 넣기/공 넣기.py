n, m = map(int,input().split())
list = [0] * n
for i in range(m):
    x,y,z = map(int,input().split())
    for j in range(x-1,y):
        list[j] = z

for i in range(n):
    print(list[i], end=" ")