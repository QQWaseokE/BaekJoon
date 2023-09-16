list = [0] * 28
num = [0] * 30
for i in range(28):
    list[i] = int(input())

for i in range(30):
    num[i] = i+1

for i in range(30):
    for j in range(28):
        if(num[i]==list[j]):
            num[i]=0

for i  in range(30):
    if(num[i]!=0):
        print(num[i])