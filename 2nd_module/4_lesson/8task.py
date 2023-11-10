cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)]
encryptedText = ""

usersText = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

for letter in usersText:
    if letter in cyrillic:
        newLetter = cyrillic[(cyrillic.index(letter) + shift) % len(cyrillic)]
        encryptedText += newLetter
    else:
        encryptedText += letter

print("Зашифрованное сообщение:", encryptedText)
