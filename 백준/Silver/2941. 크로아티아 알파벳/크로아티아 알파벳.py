def croatia_word(a):
    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    for i in croatia:
        a = a.replace(i, "!")

    print(len(a))

word = input()
croatia_word(word)