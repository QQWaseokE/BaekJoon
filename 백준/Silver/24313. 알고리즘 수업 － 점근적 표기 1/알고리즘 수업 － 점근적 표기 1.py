a1, a2 = map(int, input().split())
c = int(input())
n0 = int(input())
result = 0


for n in range(n0, 10000):
    fn = a1 * n + a2
    hn = c * n
    if fn > hn:
        result += 1

if result >= 1:
    print(0)
else:
    print(1)