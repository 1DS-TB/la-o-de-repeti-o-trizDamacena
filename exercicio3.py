N = int(input())

if N < 0:
    N *= -1
for i in range(1, 11):
    result = N * i
    print(f"{N} x {i} = {result}")