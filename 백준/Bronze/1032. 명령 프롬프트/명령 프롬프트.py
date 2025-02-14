import sys

n = int(sys.stdin.readline())
first = list(input())
result = [0] * len(first)

if n == 1:
    print("".join(first))
else:
    for _ in range(n - 1):
        others = list(input())

        for i in range(len(first)):
            if first[i] == others[i]:
                if result[i] == "?":
                    result[i] = "?"
                else:
                    result[i] = first[i]
            else:
                result[i] = "?"

    print("".join(result))
