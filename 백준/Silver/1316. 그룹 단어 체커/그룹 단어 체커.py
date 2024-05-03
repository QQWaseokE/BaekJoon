n = int(input())
result = n

for i in range(0, n):
    word = input()
    m = len(word)
    word_list = list(word)
    for j in range(0, m - 1):
        if word_list[j] == word_list[j + 1]:
            pass
        elif word_list[j] in word_list[j + 1 :]:
            result -= 1
            break

print(result)