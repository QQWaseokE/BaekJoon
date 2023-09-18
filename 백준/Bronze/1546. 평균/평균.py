# 다 더하고 최대값으로 나누고 갯수로 나누고 100곱함

n = int(input())
array = list(map(int,input().split()))
x = max(array)
y = sum(array)
z = (y/(x*n))*100

print(z)