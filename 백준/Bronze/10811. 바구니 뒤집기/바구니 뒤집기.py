n, m = map(int,input().split())

list = [0] * n
for i in range(n):
    list[i]=i+1

for i in range(m):
    x,y = map(int,input().split())
    array = list[x-1:y]
    array.reverse()
    list[x-1:y]=array

for i in range(n):
    print(list[i], end=" ")