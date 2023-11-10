text = input("Введите текст: ")
result = []
need = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
for char in text:
    if char in need:
        result.append(char)

print(f"Список гласных букв: {result}")
print(f"Длина списка: {len(result)}")