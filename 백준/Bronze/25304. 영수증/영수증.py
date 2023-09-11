total = int(input())
n = int(input())
c=0
d=0
for i in range(0,n):
    a, b = map(int,input().split())
    c=int(a)*int(b)
    d += c

if(total==d):
    print("Yes")
else : print("No")