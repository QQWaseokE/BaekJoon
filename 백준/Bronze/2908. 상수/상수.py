a, b = input().split()
c = list(a)
d = list(b)

c.reverse()
d.reverse()

if(c>d):
    print(''.join(c))
else:
    print(''.join(d))