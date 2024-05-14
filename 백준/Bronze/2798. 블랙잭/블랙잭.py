n, m = map(int, input().split())
card_list = [int(x) for x in input().split()]
result = []

for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if m >= card_list[i] + card_list[j] + card_list[k]:
                result.append(card_list[i] + card_list[j] + card_list[k])

print(max(result))