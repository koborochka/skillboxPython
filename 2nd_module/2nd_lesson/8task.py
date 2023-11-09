number = input("Введите число, чтобы добавить его; stop, чтобы закончить ввод: ")
N = []

while number != "stop":
    N.append(int(number))
    number = input("Введите число, чтобы добавить его; stop, чтобы закончить ввод: ")

print(f"Изначальный список: {N}")
N.sort()
print(f"Отсортированный список: {N}")