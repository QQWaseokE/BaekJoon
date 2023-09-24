a, b, c = map(int,input().split())

if (a==b==c):
    n = 10000 + a*1000
elif (a==b):
    n = 1000 + a*100
elif (b==c):
    n = 1000 + b*100
elif (c==a):
    n = 1000 + c*100
else:
    n = max(a,b,c)*100
    
print(n)