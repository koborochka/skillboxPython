N = int(input("Введите число: "))

list = []
for number in range(1, N+1, 2):
    list.append(number)

print(f"Список из нечётных чисел от одного до N: {list}")

