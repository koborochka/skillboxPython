N = [3, 34, 56, 1, 5, 2, 12, 12]

for index in range(len(N) - 1, -1, -1):
    if N[index] % 2 == 0:
        print(N[index], end=" ")