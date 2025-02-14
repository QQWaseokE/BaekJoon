import math

D, H, W = map(int, input().split())

n = math.sqrt((D * D) / (H * H + W * W))

h = int(H * n)
w = int(W * n)

print(h, w)
