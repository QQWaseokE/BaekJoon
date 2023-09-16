n, m = map(int,input().split())

list = [0] * n
for i in range(n):
    list[i]=i+1

for i in range(m):
    x,y = map(int,input().split())
    z=list[x-1]
    list[x-1]=list[y-1]
    list[y-1]=z

for i in range(n):
    print(list[i], end=" ")