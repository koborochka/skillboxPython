K = int(input("Сдвиг: "))
number = input("Введите число, чтобы добавить его; stop, чтобы закончить ввод: ")
N = []

while number != "stop":
    N.append(int(number))
    number = input("Введите число,чтобы добавить его, либо end, чтобы закончить ввод: ")

print(f"Изначальный список: {N}")
for i in range(K):
    N.insert(0, N.pop())

print(f"Сдвинутый список: {N}")