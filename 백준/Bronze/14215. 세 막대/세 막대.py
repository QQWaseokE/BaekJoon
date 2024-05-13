a, b, c = map(int, input().split())
num = []
two_sum = 0
num.append(a)
num.append(b)
num.append(c)

max_num = num.pop(num.index(max(num)))

for i in range(0, 2):
    two_sum += num[i]

if max_num >= two_sum:
    max_num = two_sum - 1
else:
    max_num = max_num

print(num[0] + num[1] + max_num)