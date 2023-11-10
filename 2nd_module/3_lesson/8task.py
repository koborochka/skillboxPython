numbers_count = int(input("Количество чисел: "))
sequence = []

for _ in range(numbers_count):
    sequence.append(int(input("Число: ")))

for i in range(len(sequence)):
    if sequence[i:] == sequence[i:][::-1]:
        print(f"Нужно приписать чисел: {i}")
        print(f"Сами числа: ", end="")
        print(*sequence[:i][::-1])
        break