path = input("Название файла: ")

if path.startswith(("@", "№", "$", "%", "^", "&", "*", "(", ")")):
    print("Ошибка: название начинается недопустимым символом.")
elif not(path.endswith(".txt") or path.endswith(".docx")):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно.")